#!/usr/bin/python3

import json
with open("remotehost.json") as f:
	data = json.load(f)

for j in data["hosts"]:
	print (j["host"])
