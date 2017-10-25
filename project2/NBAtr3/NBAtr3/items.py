# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class NBAtr3_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Rank = scrapy.Field()
    Team = scrapy.Field()
    _2016Season = scrapy.Field()
    Last_3 = scrapy.Field()
    Last_1 = scrapy.Field()
    Home = scrapy.Field()
    Away = scrapy.Field()
    _2015Season = scrapy.Field()
    pass
