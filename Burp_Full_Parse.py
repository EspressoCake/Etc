#!/usr/bin/env python
from lxml import etree as ET
import os
import subprocess


DATA_MANIP = """grep '<request base64="false">' /root/Desktop/XMLOUT-CLEANSED.xml | sed 's/<request base64="false">//g' | sed 's/^[ \t]*//;s/[ \t]*$//' | sort -d > /root/Desktop/CLEANSED.txt"""

def parse_file():
    x = ET.parse("/root/Desktop/test")
    output_file = open("/root/Desktop/XMLOUT-CLEANSED.xml", 'w')
    output_file.write(ET.tostring(x, pretty_print=True))
    output_file.close()
    os.system(DATA_MANIP)
    initial_open = open('/root/Desktop/FinalizedRequests.txt', 'w')
    initial_open.write("TYPE\t\tSTATUS\t\tURL\n")
    initial_open.close()
    base_Requests()


def base_Requests():
    with open('/root/Desktop/CLEANSED.txt', 'r') as file:
        for line in file.readlines():
            line = line.split()

            if line[0] == "DELETE":
                get_Deletions(line[1])
            elif line[0] == "GET":
                get_Requests(line[1])
            elif line[0] == "POST":
                get_Post(line[1])
            elif line[0] == "PUT":
                get_Put(line[1])
            else:
                continue


def get_Requests(url):
    curl_request = """curl -sL -k -w "%{http_code} %{url_effective}" -X GET --referer https://XXX.XXX.XXX.XXX:XXXX "https://XXX.XXX.XXX.XXX:XXXX""" + str(url) + """" -o /dev/null"""

    try:
        get_output = subprocess.check_output(curl_request, shell=True, executable='/bin/bash')
        print get_output
        with open('/root/Desktop/FinalizedRequests.txt', 'a') as GetRequests:
            if 200 <= int(get_output.split()[0]) <= 300:
                GetRequests.write("GET\t\t" + get_output.split()[0] + "\t\t" + get_output.split()[1] + "\n")
                GetRequests.close()

    except Exception:
        pass


def get_Deletions(url):
    curl_request = """curl -sL -k -w "%{http_code} %{url_effective}" -X "DELETE" --referer https://XXX.XXX.XXX.XXX:XXXX "https://XXX.XXX.XXX.XXX:XXXX""" + str(url) + """" -o /dev/null"""

    try:
        get_output = subprocess.check_output(curl_request, shell=True, executable='/bin/bash')
        print get_output
        with open('/root/Desktop/FinalizedRequests.txt', 'a') as GetRequests:
            if 200 <= int(get_output.split()[0]) <= 300:
                GetRequests.write("DELETE\t\t" + get_output.split()[0] + "\t\t" + get_output.split()[1] + "\n")
                GetRequests.close()

    except Exception:
        pass


def get_Post(url):
    sequential_search_output = subprocess.check_output("grep -A 12 'POST " + str(url) + "' /root/Desktop/XMLOUT-CLEANSED.xml | tail -1 | sed 's|</request>||g'", shell=True).replace("\n","")
    if sequential_search_output != "":
        curl_request = """curl -sL -k -w "%{http_code} %{url_effective}" -X "POST" --referer https://XXX.XXX.XXX.XXX:XXXX --data '""" + str(sequential_search_output) + """' "https://XXX.XXX.XXX.XXX:XXXX""" + str(url) + """" -o /dev/null"""
        try:
            get_output = subprocess.check_output(curl_request, shell=True, executable='/bin/bash')
            print get_output
            with open('/root/Desktop/FinalizedRequests.txt', 'a')  as GetRequests:
                if 200 <= int(get_output.split()[0]) <= 300:
                    GetRequests.write("POST\t\t" + get_output.split()[0] + "\t\t" + get_output.split()[1] + "\n")
                    GetRequests.close()

        except Exception:
            pass

def get_Put(url):
    sequential_search_output = subprocess.check_output("grep -A 13 'PUT " + str(url) + "' /root/Desktop/XMLOUT-CLEANSED.xml | tail -1 | sed 's|</request>||g'", shell=True).replace("\n","")
    if sequential_search_output != "":
        curl_request = curl_request = """curl -sL -k -w "%{http_code} %{url_effective}" -X "PUT" --referer https://XXX.XXX.XXX.XXX:XXXX --data '""" + str(sequential_search_output) + """' "https://XXX.XXX.XXX.XXX:XXXX""" + str(url) + """" -o /dev/null"""
        try:
            get_output = subprocess.check_output(curl_request, shell=True, executable='/bin/bash')
            print get_output
            with open('/root/Desktop/FinalizedRequests.txt', 'a')  as GetRequests:
                if 200 <= int(get_output.split()[0]) <= 300:
                    GetRequests.write("PUT\t\t" + get_output.split()[0] + "\t\t" + get_output.split()[1] + "\t\t" + sequential_search_output + "\n")
                    GetRequests.close()

        except Exception:
            pass


def cleanup_Files():
    os.system("rm /root/Desktop/CLEANSED.txt")
    os.system("rm /root/Desktop/XMLOUT-CLEANSED.xml")


parse_file()
cleanup_Files()

