# coding:utf-8
from datetime import datetime
import feedparser
import pickle
import tweepy

def string2datetime(string):
    return datetime.strptime(string.replace(' +0000', ''), '%a, %d %b %Y %H:%M:%S')

def datetime2string(dt):
    return dt.strftime('%a, %d %b %Y %H:%M:%S +0000')

class TmNCTReporter(object):
    def __init__(self, feed_url, cache_path, is_debug_mode = False):
        self.cache_path = cache_path
        self.is_debug_mode = is_debug_mode
        feed = feedparser.parse(feed_url)
        self.latest_news = [feed.entries[0].title, feed.entries[0].link, feed.entries[0].published]
        self.latest_news[2] = string2datetime(self.latest_news[2])

    def get_latest_news(self):
        return self.latest_news

    def is_updated_news(self):
        try:
            fp = open(self.cache_path + '/cache.dat')
        except IOError:
            pass

        try:
            self.local_data = pickle.load(fp)
        except:
            return True

        fp.close()

        if self.latest_news[2] > self.local_data[2]:
            if self.is_debug_mode: print "Updated"
            return True
        else:
            if self.is_debug_mode: print "Not Updated"
            return False

    def save_latest_news(self):
        try:
            fp = open(self.cache_path + '/cache.dat', 'wb')
        except IOError:
            pass
        pickle.dump(self.latest_news, fp)
        fp.close()

