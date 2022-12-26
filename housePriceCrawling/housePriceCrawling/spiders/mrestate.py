import scrapy
from .. import items 

class MrestateSpider(scrapy.Spider):
    name = 'mrestate'
    allowed_domains = ['https://mrestate.ir']
    start_urls = ['https://mrestate.ir/f/tehran/buy_residential_apartment']

    def parse(self, response):
         ads = response.css("article[class = 'w-full sm:w-1/2 xl:w-1/3 px-4 py-5']")
         for ad in ads:
            link = 'https://mrestate.ir' + ad.css("a::attr(href)").get()
            house = items.HousepricecrawlingItem(link = link)
            if link:
                print(link)
                req = scrapy.Request(url = "https://google.com" , callback= self.get_data)
                req.meta["house"] = house
                print("headerrrrr")
                yield req

    def get_data(self, response):
        print("ENTERED")
        house = response.meta["house"]
        prices = response.css("div.text-16.text-left.font-medium.text-customBlack::text").getall()
        house["total_price"] = prices[0].split(" ")[0]
        house["price"] = prices[1].split(" ")[0]
        print("AAAAAAAAAAAAAAAAAAAa",prices[0].split(" ")[0])

        yield house
