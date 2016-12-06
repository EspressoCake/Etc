#!/bin/bash 

find /var/log/* -type f -follow -print | xargs stat -c "%a %n" | sort -k1 -nr | grep -E '7[0-7][0-7]|6[1-7][1-7]' | less