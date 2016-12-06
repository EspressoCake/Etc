#!/bin/bash
# Create a New User With Sudo Privileges for Testing Purposes
# Will also add user to all known groups on a Linux host


display_usage() { 
	echo -e "\nUsage: sudo $0 [UserNameToAdd] \n" 
	} 

if [[ -z "$1" ]] || [[ $1 == "--help" ]] || [[ $USER != "root" ]]
	then
		display_usage
		exit 0
else
	PASS=`tr -dc A-Za-z0-9_ < /dev/urandom | head -c8`
	useradd -m $1
	echo "=== Your $1 user password is $PASS ==="
	echo "$1:$PASS" | chpasswd
	unset PASS
	usermod -a -G sudo $1
	for group in $(cut -d':' -f1 /etc/group); do
		usermod -a -G $group $1;
		done
	chsh -s /bin/bash $1
fi