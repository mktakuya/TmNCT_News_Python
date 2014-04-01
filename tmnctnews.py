#!/usr/bin/env python
# coding:utf-8
import sys
import tweepy
import settings
from modules.newsgetter import NewsGetter
from modules.dbconnecter import DBConnecter
from modules.botcore import BotCore

if __name__ == '__main__':
    newsgetter = NewsGetter(settings.FEED_URL)
    latest_entry_title = newsgetter.get_latest_entry_title()
    latest_entry_link = newsgetter.get_latest_entry_link()
    latest_entry_pubdate = newsgetter.get_latest_entry_pubdate()

    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    bot = BotCore(auth)

    dbconnecter = DBConnecter(settings.DB_NAME)
    dbconnecter.connect_db()
    dbconnecter.create_cursor()
    try:
        dbconnecter.create_entries_table()
    except:
        pass
    
    try:
        latest_entry_of_localdata = dbconnecter.get_latest_entry()
    except:
        dbconnecter.insert_entry(latest_entry_title, latest_entry_link, latest_entry_pubdate)
        bot.send_tweet(u"%s\n%s #苫小牧高専" % (latest_entry_title, latest_entry_link))
        sys.exit()

    if latest_entry_pubdate > latest_entry_of_localdata[2] and latest_entry_title is not latest_entry_of_localdata[0]:
        dbconnecter.insert_entry(latest_entry_title, latest_entry_link, latest_entry_pubdate)
        bot.send_tweet(u"%s\n%s #苫小牧高専" % (latest_entry_title, latest_entry_link))

