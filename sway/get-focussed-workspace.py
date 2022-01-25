#! /usr/bin/python

# This assumes that "swaymsg -rt get_workspaces" returns workspaces in the order they are
# arranged

import json
import subprocess
from sys import argv

obj = subprocess.run(["swaymsg", "-rt", "get_workspaces"], capture_output=True)
json = json.loads(obj.stdout.decode("utf-8").replace("\n", ""))

wspaces = []

for wspace in json:
    wspaces.append(wspace["name"])
    if wspace["focused"] is True:
        focussed_wspace = wspace

for x in range(len(wspaces)):
    if wspaces[x] == focussed_wspace["name"]:
        if argv[1] == "n" and x is (len(wspaces)-1):
            print(wspaces[0])
        elif argv[1] == "n":
            print(wspaces[x+1])
        elif argv[1] == "p":
            t = 2
            print(wspaces[x-1])
