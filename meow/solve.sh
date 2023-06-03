#!/usr/bin/bash
info="$(xxd -p meow.jpg | tail -n 8 | tr -d '\n' | cut -c 53-)"
echo "$info" | xxd -r -p > compressed.bin
unzip compressed.bin > /dev/null
cat flag.txt | grep -o 'FLAG{[^}]*}'
rm *.txt *.bin