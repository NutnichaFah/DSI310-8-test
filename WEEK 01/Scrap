import scrapy

class Eventseye(scrapy.Spider):
    name = "eventseye"
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
                'Describe': event.css('i::text').get(),
                'City': event.css('a.city::text').get(),
                'Place': event.css('a.place::text').get(),

            }

   
