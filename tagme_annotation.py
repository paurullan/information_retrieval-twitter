#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import requests

import gzip
import re

def get_text(text):
    key = 'i5n45r49'
    uri = "http://tagme.di.unipi.it/api"
    params = {
        'key': key,
        'text': text,
    }
    response = requests.post(uri,  data=params)
    return response.content

if __name__ == '__main__':
    filename = "data/TweetTwitter-20110912_160840.tweet.head_10.clean.gz"
    with gzip.open(filename) as f:
        for line in f.readlines():
            number = re.match("(\d+)", line).groups()[0]
            text = re.sub("\d+\s+", "", line)
            get_text(text)

