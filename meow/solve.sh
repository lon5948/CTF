#!/usr/bin/bash

binwalk -e $1 > /dev/null
cat _meow.jpg.extracted/flag.txt | grep -o 'FLAG{.*}'
rm -r _meow.jpg.extracted