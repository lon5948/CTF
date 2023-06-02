#!/usr/bin/bash

echo -e "$(strings -n 16 --data ./string | base64 -d)"