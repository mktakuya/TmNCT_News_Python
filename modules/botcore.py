# -*- coding:utf-8 -*-
import tweepy
import settings

class BotCore:
    def __init__(self, auth):
        self.auth = auth
        self.api = tweepy.API(auth_handler = self.auth, api_root = '/1.1')
        self.botname = self.auth.get_username()

    def send_tweet(self, tweet, in_reply_to = None):
        try:
            self.api.update_status(tweet, in_reply_to_status_id = in_reply_to)
        except:
            pass

