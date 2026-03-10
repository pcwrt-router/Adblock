#!/usr/bin/env python
import os
import re
import subprocess

def process_file(myfile):
    o = open("dist/%s_domains.txt" % myfile, 'w')
    with open("dist/%s.txt" % myfile, "r") as f:
        for line in iter(f):
            m = re.match(r'^\|\|(\S*)\^\s*$', line)
            if m and m.group(1) != None:
                print(m.group(1), file=o)
    o.close()

    subprocess.run(["gzip", "dist/%s_domains.txt" % myfile])
    subprocess.run("md5sum dist/%s_domains.txt.gz | cut -d ' ' -f 1 > dist/%s_domains.txt.md5" % (myfile, myfile), shell=True)

if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/%s.txt'
    files = [ 'light', 'multi', 'pro', 'pro.plus', 'ultimate' ]

    for myfile in files:
        subprocess.run(["curl", "-o", "dist/%s.txt" % myfile, url % myfile])
        process_file(myfile)
