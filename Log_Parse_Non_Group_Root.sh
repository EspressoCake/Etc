#!/bin/bash 
find /var/log* -type f -follow -print | xargs ls -l | cut -d" " -f3- | awk '$2 != "root"' | sort -k1 -d | awk '{print $1,$2,$7}' | less