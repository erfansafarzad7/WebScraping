import scrapy
from w3lib.html import remove_tags


# run => scrapy crawl bike -o bike.jl
class BikeSpider(scrapy.Spider):
    name = 'bike'
    start_urls = ['https://www.bike-discount.de/en/bike', ]

    def parse(self, response, **kwargs):
        for bike in response.css('div.product--box'):
            name = remove_tags(bike.css('a.product--title').get()).strip()
            price = remove_tags(bike.css('.product--price').get()).strip()

            yield {'name': name, 'price': price}

        next_page = response.css('a[title="Next page"]::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)
