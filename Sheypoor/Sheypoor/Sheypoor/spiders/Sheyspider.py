import scrapy
from Sheypoor.items import SheypoorItem
import time


class SheyspiderSpider(scrapy.Spider):
    name = 'Sheyspider'
    allowed_domains = ['www.sheypoor.com']
    start_urls = ['https://www.sheypoor.com/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%AE%D8%A7%D9%86%D9%87-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86']
    for i in range(2, 417):
        value = 'https://www.sheypoor.com/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%AE%D8%A7%D9%86%D9%87-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86?p=' + \
            str(i) + "&f=1672215690.0000"
        start_urls.append(value)

    def parse(self, response):
        for link in response.css('article.serp-item.list div.content h2 a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_houses)

    def parse_houses(self, response):
        item = SheypoorItem()
        item['Address'] = response.css('span.small-text::text').extract()
        item['area'] = response.css(
            'table.key-val.border-less tr')[0].css('td::text')[0].extract()
        if response.css('table.key-val.border-less tr')[1].css('th::text')[0].extract() == 'نوع ملک':
            item['type'] = response.css(
                'table.key-val.border-less tr')[1].css('td::text')[0].extract()
        else:
            item['type'] = 'Null'
        if response.css('table.key-val.border-less tr')[2].css('th::text')[0].extract() == 'تعداد اتاق':
            item['rooms'] = response.css(
                'table.key-val.border-less tr')[2].css('td::text')[0].extract()
        else:
            item['rooms'] = 'Null'
        if response.css('table.key-val.border-less tr')[3].css('th::text')[0].extract() == 'پارکینگ':
            item['parking'] = response.css(
                'table.key-val.border-less tr')[3].css('td::text')[0].extract()
        else:
            item['parking'] = 'ندارد'
        if response.css('table.key-val.border-less tr')[4].css('th::text')[0].extract() == 'انباری':
            item['warehouse'] = response.css(
                'table.key-val.border-less tr')[4].css('td::text')[0].extract()
        else:
            item['warehouse'] = 'ندارد'
        if response.css('table.key-val.border-less tr')[5].css('th::text')[0].extract() == 'آسانسور':
            item['elevator'] = response.css(
                'table.key-val.border-less tr')[5].css('td::text')[0].extract()
        else:
            item['elevator'] = 'ندارد'
        if response.css('table.key-val.border-less tr')[6].css('th::text')[0].extract() == 'سن بنا':
            item['age'] = response.css(
                'table.key-val.border-less tr')[6].css('td::text')[0].extract()
        else:
            item['age'] = 'Null'
        if response.css('table.key-val.border-less tr')[7].css('th::text')[0].extract() == 'قیمت هر متر':
            item['price'] = response.css(
                'table.key-val.border-less tr')[7].css('td::text')[0].extract()
        else:
            item['price'] = 'Null'
        item['total_price'] = response.css(
            'span.item-price strong::text').extract()
        item['Descriprion'] = response.css('p.description::text').extract()

        yield item
