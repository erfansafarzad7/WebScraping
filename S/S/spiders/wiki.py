import scrapy
from scrapy.loader import ItemLoader
from .. import items


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://www.scrapethissite.com/pages/simple/', ]

    def parse(self, response, **kwargs):
        for country in response.css('div.country'):
            l = ItemLoader(item=items.SItem(), selector=country)
            l.add_css('name', 'h3.country-name')
            l.add_css('capital', 'span.country-capital::text')
            l.add_css('population', 'span.country-population::text')

            yield l.load_item()
