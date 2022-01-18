import json
import subprocess
from sys import argv

obj = subprocess.run(["swaymsg", "-rt", "get_workspaces"], capture_output=True)
json = json.loads(obj.stdout.decode("utf-8").replace("\n", ""))

wspaces = []

for wspace in json:
    wspaces.append(wspace["num"])
    if wspace["focused"] is True:
        focussed_wspace = wspace

for x in range(len(wspaces)):
	# print(x, "-->", wspaces[x])
	if wspaces[x] == focussed_wspace["num"]:
		if argv[1] == "n":
			y = x+1
			if y == len(wspaces):
				print(wspaces[0])
			else:
				print(wspaces[y])
		elif argv[1] == "p":
			y = x-1
			if y == -1:
				print(wspaces[len(wspaces)-1])
			else:
				print(wspaces[y])
