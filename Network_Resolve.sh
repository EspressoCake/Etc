#!/bin/bash

#Create Initial Array Via Modification of Resolver
> /etc/resolv.conf
echo "hostname X.X.X.X" >> /etc/resolv.conf
echo "hostname X.X.X.X" >> /etc/resolv.conf
touch /root/initial_hosts.txt
touch /root/cleaned_host_resolution.txt

#Create Range for Query
for i in {1..254};
    echo "Searching for Host: 10.11.1.$i"
    do host -l X.X.X.$i | grep -v "not found" >> /root/resolved_hosts.txt;
done;
echo "Finished DNS Query" && echo

#Reverse Order of IP STDOut
awk -F . '{print $4"."$3"."$2"."$1" "$5$6}' /root/initial_hosts.txt > /root/cleaned_host_resolution.txt
sed -i 's/in-addrarpa domain name pointer/is/g' /root/cleaned_host_resolution.txt

#Cleanup
rm -f /root/initial_hosts.txt
echo && echo "Your File is Stored In /root/cleaned_host_resolution.txt"
