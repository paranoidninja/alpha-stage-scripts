#!/bin/bash

for d in ./*/; do (cd "$d" && echo "Updating $d" && git pull); done
