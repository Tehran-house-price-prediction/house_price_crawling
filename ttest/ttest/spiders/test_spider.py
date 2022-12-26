import scrapy
from .. import items 
import jdatetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['www.mrestate.ir']
    start_urls = ['https://mrestate.ir/f/tehran/buy_residential_apartment']

    def parse(self, response):
        ads = response.css("article[class = 'w-full sm:w-1/2 xl:w-1/3 px-4 py-5']")
        for ad in ads:
            link = 'https://www.mrestate.ir' + ad.css("a::attr(href)").get()
            house = items.TtestItem(link = link)
            if link:
                print(link)
                req = scrapy.Request(url = link , callback= self.get_data)
                req.meta["house"] = house
                yield req

        # next_page = response.css("div.bg-customBlue.text-white.rounded-md.shadow.overflow-hidden a :: attr(href)").get() # AGAIN!!: becarefull about spaces
        next_page = response.css("div.bg-customBlue.text-white.rounded-md.shadow.overflow-hidden a::attr(href)")[-1].get()
        next_page = 'https://www.mrestate.ir' + next_page
        if next_page:
            # print("NEXT PAGEEEEEEEEEEEEEEEEEEEEEEEEEEEE " , next_page)
            yield response.follow(next_page , callback = self.parse)
    def get_data(self, response):
        house = response.meta["house"]
        prices = response.css("div.text-16.text-left.font-medium.text-customBlack::text").getall()
        house["total_price"] = prices[0].split(" ")[0]
        house["price"] = prices[1].split(" ")[0]

        features = response.css("div[class = 'w-1/2 sm:w-1/4'] div[class = 'text-sm font-medium']::text")
        house["area"] = features[0].get().split(" ")[0]
        house["rooms"] = features[2].get().split(" ")[0]


        now = datetime.now()
        # jalili_date_now = jdatetime.GregorianToJalali(gday=now.day , gmonth=now.month , gyear=now.year)
        # jalili_date_now = jdatetime.date(*jalili_date_now)
        # jalili_date_built = jdatetime.date(year=int(features[1].get().split(" ")[0]) , month=1,day=1)
        house["build_year"] = features[1].get().split(" ")[1]
        house["floor"] = features[3].get().split(" ")[1] 
        house["facilities"] = "/".join(response.css("ul.flex.flex-wrap.mb-6.py-3 li div::text").getall())


        time_delta_str = response.css("div.flex.items-center.text-gray-400 p::text").get()
        house["adv_date"] = self.handle_time_delta(time_delta_str)
        house["description"] = response.css("div.flex.py-3 p::text").get()
        house["city"] = response.css("body > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)::text").get()
        house["neighbour_hood"] = response.css("body > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1)::text").get()
        yield house


    def handle_time_delta(self,time_str : str) -> str:
        if "ساعت" in time_str:
            return datetime.now().strftime("%Y-%d-%m")

        elif "روز" in time_str:
            time_delta = int(time_str.split(" ")[0])
            adv_date = datetime.now() - relativedelta(days= time_delta)
            return adv_date.strftime("%Y-%d-%m")

        elif "هفته" in time_str:
            time_delta = int(time_str.split(" ")[0])
            adv_date = datetime.now() - relativedelta(weeks= time_delta)
            return adv_date.strftime("%Y-%d-%m")

        elif "ماه" in time_str:
            time_delta = int(time_str.split(" ")[0])
            adv_date = datetime.now() - relativedelta(months= time_delta)
            return adv_date.strftime("%Y-%d-%m")





# response.css("div[class = 'w-1/2 sm:w-1/4'] div[class = 'text-sm font-medium']::text")[1].get()