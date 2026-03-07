#!/usr/bin/env python
import re
import gzip
import shutil
import subprocess

subprocess.run(["curl", "-o", "easylist.txt", "https://easylist.to/easylist/easylist.txt"])

o = open("dist/easylist-domains.txt", "w")
with open("easylist.txt", "r") as f:
    for line in f:
        m = re.match(r'^\|\|(\S*)\^\s*$', line)
        if m and m.group(1) != None:
            print(m.group(1), file=o)
o.close()

with open('dist/easylist-domains.txt', 'rb') as f_in:
    with gzip.open('dist/easylist-domains.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

subprocess.run("md5sum dist/easylist-domains.txt.gz | cut -d ' ' -f 1 > dist/easylist-domains.txt.md5", shell=True)
