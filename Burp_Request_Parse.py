#!/usr/bin/env python
from lxml import etree as ET
import os

DATA_MANIP = """grep '<request base64="false">' /root/Desktop/XMLOUT-CLEANSED.xml | sed 's/<request base64="false">//g' | sed 's/^[ \t]*//;s/[ \t]*$//' | sort -d > /root/Desktop/CLEANSED.txt"""

def parse_file():
    x = ET.parse("/root/Desktop/test")
    output_file = open("/root/Desktop/XMLOUT-CLEANSED.xml", 'w')
    output_file.write(ET.tostring(x, pretty_print=True))
    output_file.close()
    os.system(DATA_MANIP)
    os.system("rm -f /root/Desktop/XMLOUT-CLEANSED.xml")

parse_file()
