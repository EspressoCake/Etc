#!/bin/bash
#List Sudo Users Along With Available Commands Therein

cat /etc/passwd|cut -d":" -f1|sort > $1
for line in $( cat $1 ); do
    sudo -l -U $line|grep -v 'not allowed'|cut -d$'\n' -f4-
done