#!/bin/bash
#Sort all files within supplied directory by octal permission value

stat -c "%a %n" $( ls -a $1 ) | sort -nr -k1