#!/usr/bin/env python

# generates formats.json

import re
import json
import urllib

formats = []

for line in urllib.urlopen("http://www.magicdb.org/magic.db"):
    line = line.strip()
    parts = line.split("\t")
    if len(parts) != 4 or parts[0] != '0':
        continue
    m = re.match("^\[(.+)\](.+)$", parts[3])
    f = {}
    for p in m.group(1).split(";"):
        if not p: continue
        key, value = p.split("=")
        if key == "ext":
            if value:
                value = value.split(",")
            else:
                value = []
        f[key] = value
    f['description'] = m.group(2)
    formats.append(f)

print json.dumps(formats, indent=2))
