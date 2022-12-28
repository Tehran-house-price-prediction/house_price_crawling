import scrapy
from .. import items 
from datetime import datetime
from dateutil.relativedelta import relativedelta 
from .. import utils


class ShabeshSpiderSpider(scrapy.Spider):
    name = 'shabesh_spider'
    allowed_domains = ['shabesh.com']
    start_urls = ['https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86']
    page_nu = 2
    next_page= f"https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86?page={page_nu}"
    def parse(self, response):
        links_suffix = response.css(".list_announceListMode__69v30.mt-2.col-12 a::attr(href)").getall() 
        
        for link_suffix in links_suffix:
            link = 'https://www.shabesh.com' + link_suffix
            house = items.ShabeshCrawlingItem(link = link)
            if link:
                print(link)
                req = scrapy.Request(url = link , callback= self.get_data)
                req.meta["house"] = house
                yield req
        page_container = response.css("span.d-block.font-12.my-3::text").getall()
        print("**************************************************************")
        total_pages = page_container[4]
        print("t" , total_pages)
        upper_limit_page = page_container[2]
        print("ul" , upper_limit_page)
        print(ShabeshSpiderSpider.next_page)
        print("**************************************************************")
        if int(upper_limit_page) < int(total_pages):
            print("**************************ENNNTERRRRR************************************")
            yield response.follow(ShabeshSpiderSpider.next_page , callback = self.parse)
            print("YEILDDDDD")
            ShabeshSpiderSpider.page_nu +=1
    def get_data(self, response):
        # print("ENTEREEEEEEEEEEDDDDDDDD GET_DATA")
        now = datetime.now()
        house = response.meta["house"]
        features = response.css(".col-12.col-md-6 span.fw-bold::text").getall() 
        house["total_price"] = (features[4].split(" ")[0])
        house["price"] = (features[5].split(" ")[0] )
        house["area"] = (features[3])
        house["rooms"] = (features[8].split(" ")[0])
        house["build_year"] = features[7]  
        house["floor"] = features[11]
        house["neighbour_hood"] = features[6]   
        house["building_pos"] = features[9]
        house["title_type"] = features[10]
        house["total_floors"] = features[12] 
        house["houses_per_floor"] = features[14] 
        house["ac_sys"] = features[17] 
        house["heat_sys"] = features[18] 
        house["bathroom_type"] = features[13] 
        house["building_facade"] = features[16] 
        house["warm_water"] = features[19] 
        house["floor_cover"] = features[15] 
        house["city"] = "تهران"
        time_delta_str = features[20] 
        house["adv_date"] = utils.handle_time_delta(time_delta_str)
        house["facilities"] = "/".join(response.css(".announce_announceProp__eh2FN span::text").getall())
        house["description"] = response.css(".w-100.global_preLine__tKFEh.mt-4.mb-4.overflow-hidden::text").get()
        yield house
# response.css("span.d-block.font-12.my-3::text").getall()