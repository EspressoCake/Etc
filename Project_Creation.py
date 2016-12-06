__author__ = 'EspressoCake'

import os
import sys

def createDirectories():
    folders = ['Developer_Documentation', 'Draft_Reports', 'Finalized_Reports', 'Known_Vulns', 'Micellaneous_Items', 'Testing_Artifacts/Tool_Output']
    for i in folders:
        #Replace the base directory to that of your own choosing
        os.makedirs(('A:\\Directory_Of\\Your_Choice\\' + sys.argv[1] + '\\' + i), exist_ok=True)

createDirectories()