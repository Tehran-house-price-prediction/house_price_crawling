# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class SheypoorItem(scrapy.Item):
    # define the fields for your item here like:
    # input_processor = MapCompose(remove_tags), output_processo= TakeFirst()
    Address = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    area = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    type = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    rooms = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    parking = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    warehouse = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    elevator = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    age = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    total_price = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
    Descriprion = scrapy.Field(input_processor=MapCompose(
        remove_tags), output_processor=TakeFirst())
