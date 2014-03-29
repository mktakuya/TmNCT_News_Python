# coding:utf-8
import feedparser

class NewsGetter(object):
    def __init__(self, url):
        self.feed = feedparser.parse(url)
        self.latest_entry = self.feed.entries[0]

    def get_site_title(self):
        return self.feed.feed.title

    def get_latest_entry_title(self):
        return self.latest_entry.title

    def get_latest_entry_link(self):
        return self.latest_entry.link

    def get_latest_entry_pubdate(self):
        return self.latest_entry.updated

