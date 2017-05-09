#!/bin/bash

##Author : Paranoid Ninja
##Email : paranoidninja@protonmail.com
##Simple Domain Generation Algorithm Script for testing DNS Bro Scripts

temp_name=`pwgen 13 1`
nslookup $temp_name.com | grep -v 127 | grep -i -e 'Name\|Address\|NXDOMAIN'
sleep $[ ( $RANDOM % 10 )  + 1 ]s
./$0
