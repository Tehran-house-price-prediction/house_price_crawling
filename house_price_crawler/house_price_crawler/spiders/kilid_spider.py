import scrapy
from .. import items

class KilidSpiderSpider(scrapy.Spider):
    name = 'kilid_spider'
    allowed_domains = ['kilid.com']
    start_urls = ['https://kilid.com/buy-apartment/tehran?listingTypeId=1&location=272905&page=0&propertyTypeIds=2014&sort=DATE_DESC']
    page_number = 1


    def parse(self, response):
        print("new paaaaaaaaaaaaaaaaaaaaaaaaaaaaggggggggggeeee")
        links = response.css("app-listing-list-view-card[class='flex-row ng-star-inserted'] a[class='kilid-listing-card flex-col al-start ng-star-inserted']::attr(href)").getall()
        for link in links:
            link = "https://kilid.com"+link
            house = items.KilidCrawlingItem(link = link)
            req = scrapy.Request(url=link , callback= self.parse_card)
            req.meta["item"] = house

            yield req


        next_page = f"https://kilid.com/buy-apartment/tehran?listingTypeId=1&location=272905&page={KilidSpiderSpider.page_number}&propertyTypeIds=2014&sort=DATE_DESC"

        yield response.follow(next_page , callback = self.parse)
        KilidSpiderSpider.page_number+=1


    def parse_card(self, response):
        house = response.meta["item"]
        house["Description"] = response.css("span[class^='ng-tns']::text").getall()

        yield house