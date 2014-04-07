#!/usr/bin/env python
# coding:utf-8
import sys
import os
sys.path.append(os.pardir)
import unittest
from modules.tmnctreporter import TmNCTReporter
import settings_test

global news
news = None

class TmNCTReporterTest(unittest.TestCase):
    def setUp(self):
        self.reporter = TmNCTReporter(settings_test.FEED_URL,
                settings_test.CACHE_PATH, settings_test.DEBUG)

    def test_get_latest_news(self):
        news = self.reporter.get_latest_news()
        print u"""
latest_news info
    titile: {0}
    link: {1}
    published: {2}""".format(self.reporter.latest_news[0],
        self.reporter.latest_news[1], self.reporter.latest_news[2])

        self.assertTrue(news)

    def test_is_updated_news(self):
        self.reporter.latest_news = self.reporter.get_latest_news()
        self.reporter.is_updated_news()
        print u"""
local_data info
    title: {0}
    link: {1}
    published: {2}""".format(self.reporter.local_data[0], self.reporter.local_data[1], self.reporter.local_data[2])

    def test_save_latest_news(self):
        self.reporter.latest_news = self.reporter.get_latest_news()
        self.reporter.save_latest_news()

if __name__ == '__main__':
    unittest.main()

