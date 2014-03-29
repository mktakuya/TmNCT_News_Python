#!/usr/bin/env python
# coding:utf-8
import sys
import os
sys.path.append(os.pardir)
import unittest
from modules.newsgetter import NewsGetter

class GetNewsTest(unittest.TestCase):
    def setUp(self):
        self.newsgetter = NewsGetter('http://www2.tomakomai-ct.ac.jp/feed/')

    def test_feed(self):
        self.assertTrue(self.newsgetter.feed)

    def test_latest_entry(self):
        self.assertTrue(self.newsgetter.latest_entry)

    def test_get_site_title(self):
        self.assertTrue(self.newsgetter.get_site_title())

    def test_get_latest_entry_title(self):
        self.assertTrue(self.newsgetter.get_latest_entry_title())

    def test_get_latest_entry_link(self):
        self.assertTrue(self.newsgetter.get_latest_entry_link())

    def test_get_latest_entry_pubdate(self):
        self.assertTrue(self.newsgetter.get_latest_entry_pubdate())

if __name__ == '__main__':
    unittest.main()

