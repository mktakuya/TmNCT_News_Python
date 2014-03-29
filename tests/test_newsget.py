#!/usr/bin/env python
# coding:utf-8
import sys
import os
sys.path.append(os.pardir)
import unittest
from modules.newsgetter import NewsGetter

class GetNewsTest(unittest.TestCase):
    def test_getnews(self):
        self.newsgetter = NewsGetter('http://www2.tomakomai-ct.ac.jp/feed/')

        self.assertTrue(self.newsgetter.feed)
        self.assertTrue(self.newsgetter.latest_entry)
        self.assertTrue(self.newsgetter.get_site_title())
        self.assertTrue(self.newsgetter.get_latest_entry_title())
        self.assertTrue(self.newsgetter.get_latest_entry_link())
        self.assertTrue(self.newsgetter.get_latest_entry_pubdate())

if __name__ == '__main__':
    unittest.main()

