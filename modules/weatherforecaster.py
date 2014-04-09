# -*- coding:utf-8 -*-
import urllib2
import datetime
from BeautifulSoup import BeautifulStoneSoup

class WeatherForecaster:
    def __init__(self, url, area):
        response = urllib2.urlopen(url)
        soup = BeautifulStoneSoup(response)
        self.area = area
        area_weather = soup.find('area', attrs={'id': self.area})
        self.today = area_weather.find('info',
                attrs = {'date': str(datetime.date.today()).replace('-', '/')})

    def get_today_weather(self):
        return unicode(self.today.weather.renderContents(), 'utf-8')

    def get_today_max_temperature(self):
        return unicode(self.today.find('range',
            attrs={'centigrade':'max'}).renderContents(), 'utf-8')

    def get_today_min_temperature(self):
        return unicode(self.today.find('range',
            attrs={'centigrade':'min'}).renderContents(), 'utf-8')

