# coding:utf-8
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

DEBUG = True

FEED_URL = 'http://www2.tomakomai-ct.ac.jp/feed/'

CACHE_PATH = os.path.join(PROJECT_ROOT, 'cache')

if __name__ == '__main__':
    print u"""PROJECT_ROOT is {0}
FEED_URL is {1}
CACHE_PATH is {2}
""".format(PROJECT_ROOT, FEED_URL, CACHE_PATH)

