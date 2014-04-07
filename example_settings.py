# coding:utf-8
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))

DEBUG = False

FEED_URL = 'http://www2.tomakomai-ct.ac.jp/feed'

CACHE_PATH = os.path.join(PROJECT_ROOT, 'cache')

CONSUMER_KEY = 'Consumer Key'
CONSUMER_SECRET = 'Consumer Secret'
ACCESS_TOKEN = 'Access Token'
ACCESS_TOKEN_SECRET = 'Access Token Secret'

if __name__ == '__main__':
    print u"""
PROJECT_ROOT is {0}
FEED_URL is {1}
CACHE_PATH is {2}

CONSUMER_KEY is {3}
CONSUMER_SECRET is {4}
ACCESS_TOKEN is {5}
ACCESS_TOKEN_SECRET is {6}
""".format(PROJECT_ROOT, FEED_URL, CACHE_PATH, CONSUMER_KEY, CONSUMER_SECRET,
        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

