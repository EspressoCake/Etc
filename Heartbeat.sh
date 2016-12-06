#!/bin/bash
#chmod u+x 
touch ~/Ping_Hosts.txt

if [ "$1" == "" ]
then
echo "Usage: ./Ping_Hosts.sh [first_three_octets_of_network] [number_of_minutes_between_ping]"
echo "Example: ./Ping_Hosts.sh 10.67.133 2"
else
for x in `seq 1 254`; do
ping -c 1 $1.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//' >> ~/Ping_Hosts.txt
done
sleep $2m
for x in `seq 1 254`; do
ping -c 1 $1.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//' >> ~/Ping_Hosts.txt
done
fi

echo $(sort ~/Ping_Hosts | uniq -u) | xargs -n 1
rm ~/Ping_Hosts.txt