#!/bin/bash

##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : Update all git repos in current directory

for d in ./*/; do (cd "$d" && echo "Updating $d" && git pull); done
