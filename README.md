information_retrieval-twitter
=============================

Assignment for the Information retrieval course, Pisa 2011-12

The task was to capture and process a JSON collection of millions of tweets.

Notes on the material
---------------------

There is space in the machine so copy whatever you need.

In case you remove accidentally something mail me paurullan@gmail.com

These are very simple scripts so if you need any field or data just tell me.

Take into account that I gzip'ed most of the files for speed porpuses.
Some cases, like the tweet text, are not immediately gzip.

Comprensive list:

``separate_users.py``: transform the X.userinfo file into a (id, screen_name)
    input:  data/TweetTwitter-20110912_160840.usersinfo.gz
    output: data/TweetTwitter-20110912_160840.usersinfo.cleaned.gz

``parse_tweets.py``: Read the Twitter dump and separete the data into a list of
tweets for every user (id, [tweet id]) and the first cleaned tweets (tweet id,
text). This first cleaning only remove newlines and alike.

    The head_10 is an example with only the first ten lines of the original file

    input: data/TweetTwitter-20110912_160840.tweet.head_10.gz
    output: data/TweetTwitter-20110912_160840.tweet.head_10.tweet_list.gz
    output: data/TweetTwitter-20110912_160840.tweet.head_10.text

    input: data/TweetTwitter-20110912_160840.tweet.gz
    output: data/TweetTwitter-20110912_160840.tweet.tweet_list.gz
    output: data/TweetTwitter-20110912_160840.tweet.text

``clean_tweets.py`` Almost useless right now, just removes the hashes. But this
gives a good framework if we want to apply heuristics and expand the hash tag.


``TweetAnnotation.java`` (this file is found in the  ~/src directory)
        Reads the whole cleaned file and queries TAGME.
        The output format is (tweet_id, [# Annotation])
    
        input: /l/disc3/home/ir2011/paurullan/data/TweetTwitter-20110912_160840.tweet.head_10.clean
        output: /l/disc3/home/ir2011/paurullan/data/TweetTwitter-20110912_160840.tweet.head_10.annotation
