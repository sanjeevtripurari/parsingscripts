#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
        filename = sys.argv[1]
else:
	filename="remote-hosts.conf"

with open(filename) as f:
	content=f.readlines()

for line in content:
	print(line)
