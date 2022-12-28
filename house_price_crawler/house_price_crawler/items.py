# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousePriceCrawlerItem(scrapy.Item):
    price = scrapy.Field()
    total_price = scrapy.Field()
    link = scrapy.Field()
    area = scrapy.Field()
    facilities = scrapy.Field()
    build_year = scrapy.Field() # Its better to use build year and calc building age in piplines of creating model
    neighbour_hood = scrapy.Field()
    rooms = scrapy.Field()
    floor = scrapy.Field()
    description = scrapy.Field()
    # address = scrapy.Field()
    adv_date = scrapy.Field()
    city = scrapy.Field()
    # latitude  = scrapy.Field() ## north/south
    # longitude  = scrapy.Field() ## west/east  
    # lat/long



class ShabeshCrawlingItem(scrapy.Item):
    price = scrapy.Field()
    total_price = scrapy.Field()
    link = scrapy.Field()
    area = scrapy.Field()
    facilities = scrapy.Field()
    build_year = scrapy.Field() 
    neighbour_hood = scrapy.Field()
    rooms = scrapy.Field()
    floor = scrapy.Field()
    description = scrapy.Field()
    adv_date = scrapy.Field()
    city = scrapy.Field()
    building_pos = scrapy.Field()
    title_type  = scrapy.Field()
    total_floors = scrapy.Field()
    houses_per_floor = scrapy.Field()
    ac_sys = scrapy.Field()
    heat_sys = scrapy.Field()
    bathroom_type = scrapy.Field()
    building_facade = scrapy.Field()
    warm_water = scrapy.Field()
    floor_cover = scrapy.Field()
