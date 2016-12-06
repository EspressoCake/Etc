#!/usr/bin/env python

from socket import *
from itertools import permutations
import time
import sys

ip = sys.argv[1]

def Knockport(ports):
    for port in ports:
        try:
            print "[*] Knocking on Port: ", port
            s2 = socket(AF_INET, SOCK_STREAM)
            s2.settimeout(0.1)
            s2.connect_ex((ip, port))
            s2.close()
        except Exception, e:
            print "[-] %s" % e

def main():
    r = [7, 23, 50, 2350, 43]
    for comb in permutations(r):
        print "\n[*] Trying Sequence %s" % str(comb)
        Knockports(comb)
    print "[*] Done! Check for Open"
    
main()