#!/usr/bin/bash

echo -e "$(strings -n 16 --data $1 | head -n 1 | base64 -d)"
