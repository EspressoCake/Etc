#!/bin/bash
#By Justin

COLOR=`tput setaf 2`
DATAPOINTS='^[0-9]+$'

if [ "$#" -ne 2 ]; then
    echo -e "${COLOR}Please Supply Two Arguments, Representing Range Start and End!"
    echo -e "${COLOR}Example: $0 1 255"
    exit 1
fi

if ! [[ $1 =~ $DATAPOINTS ]] || ! [[ $2 =~ $DATAPOINTS ]]; then
    echo -e "${COLOR}At Least One of Your Arguments Is Not A Number!"
    exit 1
else
    > /etc/resolv.conf
    echo "nameserver 10.11.1.220" > /etc/resolv.conf
    echo "nameserver 10.11.1.221" > /etc/resolv.conf
    touch /root/HOSTS_RESOLVED.txt
    for IP in $(eval echo {$1..$2}); do
        echo "Attemping to Resolve: 10.11.1.$IP"
        host -l 192.168.1.$IP | grep -v "not found" >> $PWD/HOSTS_RESOLVED.txt
    done
fi

awk -F "." '{print $4"."$3"."$2"."$1,"is"$5,$6}' $PWD/HOSTS_RESOLVED.txt | echo $(sed -e 's/in-addr arpa domain name pointer//g' > $PWD/HOSTS_RESOLVED.txt)

echo && echo "${COLOR}Your Hostname Resolution Has Completed!" && echo "To View Contents, Type cat $PWD/HOSTS_RESOLVED.txt"
