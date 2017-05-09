#!/bin/bash

##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : Display size of packets per second received on a network interface

if [ -z "$1" ]; then
        echo
        echo usage: $0 network-interface
        echo
        echo e.g. $0 wlp1s0
        echo
        exit
fi

IF=$1

while true
do
        R1=`cat /sys/class/net/$1/statistics/rx_bytes`
        T1=`cat /sys/class/net/$1/statistics/tx_bytes`
        sleep 1
        R2=`cat /sys/class/net/$1/statistics/rx_bytes`
        T2=`cat /sys/class/net/$1/statistics/tx_bytes`
        TBPS=`expr $T2 - $T1`
        RBPS=`expr $R2 - $R1`
        TKBPS=`expr $TBPS / 1024`
        RKBPS=`expr $RBPS / 1024`
        echo "tx $1: $TKBPS kb/s rx $1: $RKBPS kb/s"
done
