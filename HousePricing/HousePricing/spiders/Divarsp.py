import scrapy


class DivarspSpider(scrapy.Spider):
    name = 'Divarsp'
    allowed_domains = ['divar.ir']
    start_urls = ['http://divar.ir/']

    def parse(self, response):
        pass
