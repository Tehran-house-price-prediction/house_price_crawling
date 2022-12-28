# house_price_crawling
Crawl data for house price detection from web apps
# Notes
1.in setting.py ----> FEED_EXPORT_ENCODING = 'utf-8'
2.take care of spaces ---> a :: text --> raises error --> a::text
3.for requests, url format is https://www.sitename.domain
4.[] notation is available for css selectors ----> dic[class = 'pads : 2 ']
5.use selectorshub extension to easily grab css or xpath

6.to have shell splash response:
scrapy shell 'http://localhost:8050/render.html?url=http://example.com/page-with-javascript.html&timeout=10&wait=0.5'
7. Added DOWNLOAD_DELAY = 3 in setting.py