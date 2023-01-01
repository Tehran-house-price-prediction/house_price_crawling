import scrapy
from .. import items , utils
from datetime import datetime
from scrapy_splash import SplashRequest
import urllib.parse


class IranfileSpiderSpider(scrapy.Spider):
    name = 'iranfile_spider'
    allowed_domains = ['iranfile.ir']
    start_urls = ['https://iranfile.ir/Search/F8F3E815/%D8%AE%D8%B1%DB%8C%D8%AF_%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86_%D8%AA%D9%87%D8%B1%D8%A7%D9%86']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url= url , callback= self.parse , args={"wait" : 3})


    def parse(self, response):
        links = response.xpath("//tbody/tr//a/@href").getall()
        # print(links)
        for link in links:
            link = urllib.parse.quote(link, safe = ':/',encoding="utf-8")
            house = items.IranfileCrawlingItem(link=link)
            if link:
                # print(link)
                req = scrapy.Request(url =link  , callback= self.get_data)
                req.meta["house"] = house
                yield req



    def get_data(self, response):
        house = response.meta["house"]
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
        # print(len(response.css("div.file-data::text").getall()) )
        properties = response.css("span.file-data::text").getall() 
        
        # print(response.xpath("//span[@class='file-data for-print']/text()").get()) # NOT WORKING

        house["total_price"] = "/".join(properties)
        # house["price"] = properties[5].split()[0]

        # house["area"] = features[0].get().split(" ")[0]
        # house["rooms"] = features[2].get().split(" ")[0]


        # now = datetime.now()
        # # jalili_date_now = jdatetime.GregorianToJalali(gday=now.day , gmonth=now.month , gyear=now.year)
        # # jalili_date_now = jdatetime.date(*jalili_date_now)
        # # jalili_date_built = jdatetime.date(year=int(features[1].get().split(" ")[0]) , month=1,day=1)
        # house["build_year"] = features[1].get().split(" ")[1]
        # house["floor"] = features[3].get().split(" ")[1] 
        # house["facilities"] = "/".join(response.css("ul.flex.flex-wrap.mb-6.py-3 li div::text").getall())


        # time_delta_str = response.css("div.flex.items-center.text-gray-400 p::text").get()
        # house["adv_date"] = properties[0]
        house["description"] = response.css("script::text")[1].get()
        # # house["city"] = response.css("body > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)::text").get()
        # house["neighbour_hood"] = properties[3].strip()
        # house["houses_per_floor"] = features[14]
        # house["total_floors"] = features[12] 
        # house["build_year"] = features[7]  
        # house["building_facade"] = features[16] 
        house["title_type"] = response.css("script::text")
        house["description"] = "/".join(response.css("td::text").getall())  + "/".join(response.css("td i::attr(class)").getall() )

        yield house

