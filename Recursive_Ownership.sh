#!/bin/bash
#Recursively search default RHEL/CentOS log directory for files not owned by root

find /var/log* -type f -follow -print | xargs ls -l | cut -d" " -f3- | awk '$1 != "root"' | sort -k1 -d | awk '{print $1,$2,$7}' | less
