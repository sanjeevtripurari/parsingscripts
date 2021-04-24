#!/usr/bin/python3

import getopt, sys

def usage():
	print("Usage:\n\tpygetopts.py -f filename")
	
opts, args = getopt.getopt(sys.argv[1:], "f:h", ["filename=","help"])


for o, a in opts:
	if o in ("-f", "--filename"):
		filename=a
	elif o in ("-h", "--help"):
		usage()
		sys.exit()

with open(filename) as f:
        content=f.readlines()

for line in content:
	print(line.rstrip())

