import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# https://www.eventseye.com/fairs/t1_trade-shows_jewellery-watch-making-gifts.html
#https://www.eventseye.com/fairs/f-fashionista-lifestyle-exhibition-rajkot-28346-1.html



class Eventseye(scrapy.Spider):
    name = "eventseye"
    # start_urls = ['https://www.eventseye.com/fairs/st1_trade-shows_jewelry.html']
    start_urls = [
        'https://www.eventseye.com/fairs/st1_trade-shows_jewelry.html',
        'https://www.eventseye.com/fairs/st1_trade-shows_jewelry_1.html',
        'https://www.eventseye.com/fairs/st1_trade-shows_jewelry_2.html',
        'https://www.eventseye.com/fairs/st1_trade-shows_jewelry_3.html'
    ]

    def parse(self, response):
        for event in response.css('tr'):
            yield {
                'Exhibition_Name': event.css('b::text').get(),
                'describe': event.css('i::text').get(),
                'city': event.css('a.city::text').get(),
                'place': event.css('a.place::text').get(),

            }

   