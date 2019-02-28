# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class PredioItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()

    url = scrapy.Field()


class PredioItemLoader(ItemLoader):
    default_item_class = PredioItem

