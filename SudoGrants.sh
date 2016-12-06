#!/bin/bash

touch /$USER/output
cat /etc/passwd|sort -d -k1 | cut -f1 -d':' >> /$USER/output
cat /$USER/output|while read line; do
    sudo -l -U $line | grep -v 'not allowed'|cut -d$'\n' -f3-5;
done
rm -f /$USER/output
shred -u $0