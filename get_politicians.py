#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import codecs
import json
import twitter

def get_tweets(api, user):
    tweets = api.GetUserTimeline(user, 200, 2010-01-01)
    return tweets

def get_user(api, user):
    json_dump = { 
        "user": user,
        #"tweets": map(lambda x: x.AsJsonString(), get_tweets(api, user)),
        "tweets": map(lambda x: x.AsDict(), get_tweets(api, user)),
        }
    return json_dump

if __name__ == '__main__':
    politicians = [
        52352494,
        18762875,
        97734603,
        314059678,
        14078646,
        19067940,
        17336414,
    ]
    api = twitter.Api()
    politician_tweets = map(lambda x: get_user(api, x), politicians)
    with open("politician_tweets", 'w') as f:
        for politician in politician_tweets:
            json.dump(politician, f)
            f.write("\n")

