# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GenreItem(scrapy.Item):
    gname = scrapy.Field()
    gdesc = scrapy.Field()
    glink = scrapy.Field()