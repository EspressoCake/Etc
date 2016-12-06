#!/usr/bin/env python

import xml.etree.cElementTree as ET
import subprocess
import string
import re
import sys
import random


def radamsa_random():
    text = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(1, (random.randint(1, 200))))
    output = subprocess.check_output('echo "' + text + '" | radamsa', shell=True).decode('utf-8','ignore')
    return output

def create_files():
	if len(sys.argv) < 2 or len(sys.argv) > 2:
			print "USAGE: " + sys.argv[0] + " number_of_files_to_make"
			sys.exit()
	else:
		if sys.argv[1] != "":
			for i in range(1, int(sys.argv[1])+ 1):
				root = ET.Element("root")
				doc = ET.SubElement(root, "document")
				ET.SubElement(doc, "subsection1", name="subs1").text = radamsa_random()
				ET.SubElement(doc, "subsection2", name="subs2").text = radamsa_random()
				tree = ET.ElementTree(root)
				tree.write("/root/Desktop/RadamsaFiles/file" + str(i) + ".xml")

create_files()