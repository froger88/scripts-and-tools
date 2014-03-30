#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pymongo

import config

api_key=config.api_key
api_secret=config.api_secret

access_token=config.access_token
access_token_secret=config.access_token_secret


mongocl = pymongo.MongoClient()['mongo-1']
counter = 0

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        global counter
        global mongocl
        if counter == config.max_count:
            print "finished"
            exit(0)

        counter += 1
        json_data = json.loads(data)
        #print json_data
        mongocl[config.task_id].insert(json_data)
        print "\r%d" % counter,
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=config.keywords, languages=config.languages)
