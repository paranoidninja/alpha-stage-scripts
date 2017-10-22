#!/bin/bash

##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : Get Public IP Address

IP=`dig +short myip.opendns.com @resolver1.opendns.com 2>/dev/null`
if [ -z "$IP" ]; then
	echo "Status: Disconnected"
else
	echo "IP: $IP"
fi

