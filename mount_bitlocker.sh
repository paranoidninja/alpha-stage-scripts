#!/bin/bash

##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : Mount Bitlocker at mounted location

mountee="/media/armory_locker"
mounted="/media/armory_mounted"

if [[ $EUID == 0 ]]; then
	bitpart=`fdisk -l | egrep "HPFS|NTFS" | cut -f 1 -d" "`
	echo $bitpart
	mkdir $mountee
	mkdir $mounted
	sudo dislocker -r -V $bitpart -u -- $mountee
	mount -r -o loop /media/armory_locker/dislocker-file /media/armory_mounted
	echo -e "Mounted at $mounted\n"
fi
