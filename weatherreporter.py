#!/usr/bin/env python
# coding:utf-8
import datetime
from modules.weatherforecaster import WeatherForecaster
from modules.tweetman import TweetMan
import settings

if __name__ == '__main__':
    try:
        logger = open('./weatherlog.log', 'a')
    except IOError:
        pass

    logger.write(u"Start WeatherForecaster at {0}\n".format(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")))

    reporter = WeatherForecaster(settings.WEATHER_XML_URL, settings.WEATHER_AREA_NAME)
    today_weather = reporter.get_today_weather()
    today_max_temperature = reporter.get_today_max_temperature()
    today_min_temperature = reporter.get_today_min_temperature()

    tweetman = TweetMan(settings.CONSUMER_KEY, settings.CONSUMER_SECRET,
            settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    tweet = u"""{today}の{area}
    天気：{weather},
    最高気温：{max_temp}℃,
    最低気温：{min_temp}℃""".format(today = unicode(datetime.date.today()).replace('-', '/'),
            area = settings.WEATHER_AREA_NAME, weather = today_weather,
            max_temp = today_max_temperature, min_temp = today_min_temperature)

    if tweetman.send_tweet(tweet):
        logger.write(u"conpleted send_tweet!\n")
    else:
        logger.write(u"send_tweet missing...\n")

    logger.write(u"End.\n\n")
    logger.close()

