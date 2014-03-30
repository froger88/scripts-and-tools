#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import config

api_key=config.api_key
api_secret=config.api_secret

access_token=config.access_token
access_token_secret=config.access_token_secret

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print type(data)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=config.keywords, languages = config.languages)
