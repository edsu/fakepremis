#!/usr/bin/env python

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
        kv = p.split("=")
        if len(kv) == 2:
            f[kv[0]] = kv[1]
    f['description'] = m.group(2)
    formats.append(f)

open("formats.json", "w").write(json.dumps(formats, indent=2))
