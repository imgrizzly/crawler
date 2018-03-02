# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SmallcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影链接，电影名，导演，演员，imdb链接，上映时间，语言，剧情简介
    filmname = scrapy.Field()
    director = scrapy.Field()
    performer = scrapy.Field()
    imdb = scrapy.Field()
    release_time = scrapy.Field()
    language = scrapy.Field()
    synopsis = scrapy.Field()
    pass
