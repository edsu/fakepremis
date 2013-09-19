#!/usr/bin/env python

import os
import json

def load_json(filename):
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    return json.loads(open(f).read())

events = load_json("events.json")
formats = load_json("formats.json")



