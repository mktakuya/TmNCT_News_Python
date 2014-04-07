#!/usr/bin/env python
# coding:utf-8
from datetime import datetime
from modules.tmnctreporter import TmNCTReporter
from modules.tweetman import TweetMan
import settings

if __name__ == '__main__':
    try:
        logger = open('./reportlog.log', 'a')
    except IOError:
        pass

    logger.write(u"Start TmNCT_News at {0}\n".format(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")))

    reporter = TmNCTReporter(settings.FEED_URL, settings.CACHE_PATH)

    if reporter.is_updated_news():
        logger.write(u"Updated!!\n")
        reporter.save_latest_news()
        tweetman = TweetMan(settings.CONSUMER_KEY, settings.CONSUMER_SECRET,
                settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
        tweet = u"{0}\n{1} #苫小牧高専".format(reporter.latest_news[0],
                reporter.latest_news[1])
        if not tweetman.send_tweet(tweet) is False:
            logger.write(u"completed send_tweet!\n")
        else:
            logger.write(u"send_tweet missing...\n")
    else:
        logger.write('Not Updated...\n')

    logger.write(u"End.\n\n")
    logger.close()

