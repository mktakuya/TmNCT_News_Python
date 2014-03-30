#!/usr/bin/env python
# coding:utf-8
import sys
import os
sys.path.append(os.pardir)
import unittest
import tweepy
from modules.botcore import BotCore
import settings

class TwitterOAuthTest(unittest.TestCase):
    def test_twitter_oauth(self):
        auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
        self.bot = BotCore(auth)
        self.assertTrue(self.bot)

if __name__ == '__main__':
    unittest.main()

