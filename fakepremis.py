#!/usr/bin/env python

import os
import json
import config
import random
import tweepy

# fakepremis will only tweet this percent of the time which is useful to 
# inject the appearance of randomness if it is running from cron

LIKELIHOOD = 20 

def premis():
    ev = event()
    fo = format()
    fn = filename(fo)
    ag = agent()
    msg = "%s event for file %s by %s" % (ev, fn, ag)

    if ev == "format identification":
        ag = fileidagent()
        msg = "%s event for file %s by %s ; result: %s" % (ev, fn, ag, fo['description'])
    elif 'check' in ev:
        msg += " ; result: " + random.choice(["PASS", "FAIL"])
    return msg

def load_json(filename):
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', filename)
    return json.loads(open(f).read())

def rnd(l):
    return l[random.randint(0, len(l)-1)]

def filename(fmt=None):
    name = ""
    while len(name) < 15:
        name += rnd(words).lower()
    if not fmt:
        fmt = format()
    if len(fmt["ext"]) > 0:
        name = "%s.%s" % (name, fmt["ext"][0])
    return name

def fileid():
    return rnd(fileidagents)

def event():
    return rnd(events)

def format():
    return rnd(formats)

def agent():
    return rnd(agents)

def fileidagent():
    return rnd(fileidagents)

def tweet(msg):
    auth = tweepy.OAuthHandler(config.twitter_oauth_consumer_key, 
                               config.twitter_oauth_consumer_secret)
    auth.set_access_token(config.twitter_oauth_access_token_key,
                          config.twitter_oauth_access_token_secret)
    twitter = tweepy.API(auth)
    twitter.update_status(msg)

events = load_json("events.json")
formats = load_json("formats.json")
words = load_json("words.json")
agents = load_json("agents.json")
fileidagents = load_json("fileidagents.json")

if __name__ == "__main__":
    if random.randint(0, 100) <= LIKELIHOOD:
        tweet(premis())
