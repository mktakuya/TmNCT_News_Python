# coding:utf-8
import sqlite3

class DBConnecter(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def connect_db(self):
        self.conn = sqlite3.connect(self.db_name)

    def create_cursor(self):
        self.cur = self.conn.cursor()

    def create_entries_table(self):
        self.cur.execute(
                """CREATE TABLE entries"""
                """(id serial, title text, link text, pub_date text);"""
                )

    def insert_entry(self, title, link, pub_date):
        latest_entry = (title, link, pub_date)
        self.cur.execute(
                """INSERT INTO entries(title, link, pub_date) VALUES(?, ?, ?);""",
                latest_entry
                )

    def get_latest_entry_pub_date(self):
        self.cur.execute(
                """SELECT title, link, MAX(pub_date) FROM entries"""
                )
        self.latest_entry = self.cur.fetchone()
        return self.latest_entry

    def close_connection(self):
        self.conn.commit()
        self.conn.close()

