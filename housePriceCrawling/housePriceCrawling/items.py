# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousepricecrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # area = scrapy.Field()
    # facilities = scrapy.Field()
    # build_year = scrapy.Field()
    # neighbour_hood = scrapy.Field()
    # rooms = scrapy.Field()
    # floor = scrapy.Field()
    # description = scrapy.Field()
    # address = scrapy.Field()
    price = scrapy.Field()
    total_price = scrapy.Field()
    link = scrapy.Field()
    
