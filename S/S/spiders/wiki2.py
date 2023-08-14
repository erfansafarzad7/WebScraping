import scrapy


class Wiki2Spider(scrapy.Spider):
    name = "wiki2"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Chicken"]

    def parse(self, response, **kwargs):
        pass
