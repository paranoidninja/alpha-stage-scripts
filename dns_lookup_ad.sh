#!/bin/bash

##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : A Script to gather hostnames of machines within a domain

i="0"

while [ $i -lt "255" ]
do nslookup 10.11.1.$i 10.11.1.220 | grep -v "NXDOMAIN" | grep name | cut -f1,3 -d" "
	i=$[ $i+1 ]
done
