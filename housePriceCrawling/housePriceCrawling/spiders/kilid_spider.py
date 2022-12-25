import scrapy


class KilidSpiderSpider(scrapy.Spider):
    name = 'kilid_spider'
    allowed_domains = ['kilid.com']
    start_urls = ['http://kilid.com/']

    def parse(self, response):
        pass
