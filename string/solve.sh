#!/usr/bin/bash

echo -e "$(strings -n 16 -d $1 | head -n 1 | base64 -d)"
