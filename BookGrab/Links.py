import os
import requests
import subprocess
from BeautifulSoup import BeautifulSoup, SoupStrainer
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter


def Grab():
    url = "http://advancedlinuxprogramming.com/alp-folder/"
    http_request = requests.get(url)
    http_data = http_request.text
    soup = BeautifulSoup(http_data)

    for link in soup.findAll('a'):
        if "alp-ch" in link.get('href'):
            print "Grabbing %s" % str(link.get('href'))
            os.system("wget {0} > /dev/null 2>&1".format(url + link.get('href')))


def PDF_Merge():
    print "\nMerging PDFs..."
    current_directory = subprocess.check_output("pwd", shell=True).strip()
    pdf_files = [f for f in os.listdir(current_directory) if f.endswith("pdf")]
    merger = PdfFileMerger()
    for f in pdf_files:
        merger.append(PdfFileReader(os.path.join(current_directory, f), 'rb'))
    merger.write(os.path.join(current_directory, "Advanced_Linux.pdf"))
    print "Done!"
    
    print "\nCleaning Files..."
    [os.remove(os.path.join(current_directory, f)) for f in os.listdir(current_directory) if f.startswith("alp-ch")]
    print "Done!"


if __name__ == '__main__':
    Grab()
    PDF_Merge()
