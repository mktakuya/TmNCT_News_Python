#!/usr/bin/env python
# coding:utf-8
import sys
import os
sys.path.append(os.pardir)
import unittest
from datetime import datetime
from modules.dbconnecter import DBConnecter

class DBConnectTest(unittest.TestCase):
    def setUp(self):
        self.dbconnecter = DBConnecter('sqlite3test.db')
        self.dbconnecter.connect_db()
        self.dbconnecter.create_cursor()

    def tearDown(self):
        self.dbconnecter.close_connection()

    def test_create_entries_table(self):
        try:
            self.dbconnecter.create_entries_table()
        except:
            pass

    def test_insert_entry(self):
        now = datetime.now()
        self.dbconnecter.insert_entry(u'テストタイトル',
                u'http://example.com/entry/1111',
                now.strftime('%Y-%m-%d %H:%M:%S'))

    def test_get_latest_entry_pub_date(self):
        actual = self.dbconnecter.get_latest_entry_pub_date()
        self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main()

