# coding:utf-8
import tweepy

class TweetMan(object):
    def __init__(self, consumer_key, consumer_secret, access_token,
            access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def send_tweet(self, tweet, in_reply_status_id = None):
        self.api.update_status(tweet, in_reply_status_id)

