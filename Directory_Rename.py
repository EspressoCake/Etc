#For Corey

import os
import sys
import string

def data_rename(path):
    data = os.listdir(path.replace("\", "/"))
    for item in data:
        if "&" in item:
            os.rename(item, item.replace("&", " "))
            print "Fixed item %s" % item
        else:
            continue

data_rename(sys.argv[1])