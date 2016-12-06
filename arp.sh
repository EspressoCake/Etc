#!/bin/bash
#Perform and ARP sweep of the network of your choosing

PREFIX=$1
INTERFACE=$2

display_usage() {
    echo -e "\nUsage: $0 [PREFIX] [INTERFACE]\n"
    echo -e "Example: $0 192.168 eth0\n"
    }

if [[ -z "$1" ]] || [[ -z "$2" ]] || [[ $1 == "--help" ]]
    then
        display_usage
        exit 0
else
    for SUBNET in {1..255}
    do
        for HOST in {1..255}
        do
            echo "[*] IP: "$PREFIX"."$SUBNET"."$HOST
            arping -c 3 -i $INTERFACE $PREFIX"."$SUBNET"."$HOST 2>/dev/null
        done
    done
fi