from lxml import etree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import xml.etree.cElementTree as cET
import subprocess
import string
import re
import random
import sys
import os
import time

#Create random seed for Radamsa, and return the value when run against Radamsa
def random_string_generator(number):
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(1, (random.randint(1, number))))

#Create Radamsa Values
def radamsa_random():
    text = random_string_generator(100)
    output = subprocess.check_output('echo "' + text + '" | radamsa', shell=True).decode('utf-8','ignore')
    return output

#Create name for compressed file, should the user elect to create one
def compressed_file_name():
	return (time.strftime("%B_%d_%H_%M"))

#Create archive with compression in user's root directory, should they elect to
def compress_files():
	if len(sys.argv) == 4:
		if sys.argv[3] == 'Y':
			print "\nCompressing..."
			os.system('tar -zcvf ~/' + compressed_file_name() + '.tar.gz %s' % sys.argv[2])
			print "\nCompression successful!"
			print "\nThe compressed archive is here: " + sys.argv[2] + compressed_file_name() + ".tar.gz"
		else:
			print "\nSkipping compression and archiving, have a nice day!"
			print "\nYour files are in: %s" % sys.argv[2]
	else:
		print "\nAll done!"
		print "Your files are in: %s" % sys.argv[2]		
		sys.exit()

#Use Radamsa output to build shell XML document, with a randomly generated amount of child nodes
def create_files():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
            print "USAGE: python " + sys.argv[0] + " [number_of_files_to_make]" + " [directory_to_save_to]" + " [compress_into_archive]"
            print "EXAMPLE: python " + sys.argv[0] + " 20 ~/Desktop/File_Folder/ Y"
            sys.exit()
    else:
	counter = 1
        if sys.argv[1] != "" and sys.argv[2] != "":
            for i in range(1, int(sys.argv[1])+ 1):
                try:
                    root = cET.Element("root")
                    doc = cET.SubElement(root, "document")
                    cET.SubElement(doc, "subsection1", name="subs1").text = radamsa_random()
                    cET.SubElement(doc, "subsection2", name="subs2").text = radamsa_random()
                    users = cET.SubElement(doc, random_string_generator(30), name= random_string_generator(30)).text = radamsa_random()
                    for x in range(1, random.randint(10, 20)):
				        locals()['users_{0}'.format(x)] = cET.SubElement(doc, random_string_generator(30), name= random_string_generator(30)).text = radamsa_random()
                    tree = cET.ElementTree(root)
                    tree.write(sys.argv[2] + str(i) + ".xml")
                    print "File Created Successfully #: %s" % counter
		    counter += 1
				
		except subprocess.CalledProcessError:
                    continue
		
"""Create a list of files to be manipulated in following function"""
def open_files():
	files = []    
	for matching_items in os.listdir(sys.argv[2]):
		if matching_items.endswith(".xml"):
			files.append(os.path.join(sys.argv[2], matching_items))
	return sorted(files)
    
"""Parse files in directory from standard input and modify them as needed"""
def herein():
	counter = 0
	for documents in open_files():
		try:
			magical_parser = ET.XMLParser(encoding='utf-8', recover=True)	
			document = ET.parse(documents, magical_parser)
			testing = document.getroot()
			users = SubElement(testing, 'test', name= random_string_generator(30)).text = radamsa_random()
			for x in range(1, random.randint(10, 20)):
				locals()['users_{0}'.format(x)] = SubElement(testing, random_string_generator(30), name= random_string_generator(30)).text = radamsa_random()			
			output_file = open(documents, 'w')
			output_file.write(ET.tostring(testing, pretty_print=True))
			output_file.close()
			print "Succesfully Created File #: %s" % counter
			counter += 1
		except ValueError:
			print "Succesfully Created File #: %s" % counter
			counter += 1			
			continue		            


create_files()
compress_files()