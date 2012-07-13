#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module is completely stupid right now: it only remove the hashes (#)
and this could be more easily done with a sed. The purpouse is to have in
the future things like an url expander or a hash tag processor.

"""

import codecs
import re
import os
import gzip

class TweetCleaner(object):

    def __init__(self, filename=None):
       if not filename:
           filename = "data/TweetTwitter-20110912_160840.tweet.head_10.text"
       self.text_filename = filename
       name, ext = os.path.splitext(filename)
       self.clean_filename = name + ".clean"

    def clean(self, text):
        """Cleaning of text.
            1. remove '#'
        """
        # this seems to be too simple but it is in future perspective


    def clean_and_save_text(self):
        """Since the data is so big we have to do this on the fly"""
        text_file = codecs.open(self.text_filename, 'r', 'utf-8')
        clean_file = codecs.open(self.clean_filename, 'w', 'utf-8')
        for line in text_file:
            text = self.clean(line)
            clean_file.write(text)
        text_file.close()
        clean_file.close()


if __name__ == '__main__':
    real_dataset = "data/TweetTwitter-20110912_160840.tweet.text"
    cleaner = TweetCleaner(real_dataset)
    #cleaner = TweetCleaner()
    cleaner.clean_and_save_text()

