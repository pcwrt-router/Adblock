#!/usr/bin/env python
import re
import subprocess

subprocess.run(["curl", "-o", "easylist.txt", "https://easylist.to/easylist/easylist.txt"])

o = open("easylist-domains.txt", "w")

with open("easylist.txt", "r") as f:
    for line in f:
        m = re.match(r'^\|\|(\S*)\^\s*$', line)
        if m and m.group(1) != None:
            print(m.group(1), file=o)

o.close()
