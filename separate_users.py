#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import gzip

def extract(user):
    """Returns the id, name from the json data"""
    j_form = json.loads(user)
    twitter_id, screen_name = j_form['id'], j_form['screen_name']
    return twitter_id, screen_name


def extract_users_from_files(data_filename, save_filename):
    """Read the userinfo and leaves a (id, screen_name) summary"""
    with gzip.open(data_filename) as source_data:
        user_data = map(extract, source_data.readlines())

    with gzip.open(save_filename, 'w') as save_file:
        for user_id, user_name in user_data:
            save_file.write("{0} {1}\n".format(user_id, user_name))


if __name__ == '__main__':
    # The program expects a gzip file
    # expect 15/1 ratio. If not, check why
    data = "data/TweetTwitter-20110912_160840.usersinfo.gz"
    save = "data/TweetTwitter-20110912_160840.usersinfo.cleaned.gz"
    extract_users_from_files(data, save)

