import scrapy
from scrapy.crawler import CrawlerProcess


class FdSpider(scrapy.Spider):
    name = 'fd'

    def start_requests(self):
        yield scrapy.Request('https://faradars.org/how-to-learn/programming')

    def parse(self, response, **kwargs):
        for fara in response.css('div.flex-wrap:nth-child(3)'):
            title = fara.css('div.mb-3:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > h2:nth-child(1)::text').get()
            yield {'title': title}


process = CrawlerProcess(settings={
    'FEEDS': {
        'home/desktop/fara.json': {'format': 'json', 'encoding': 'utf8'},
        'home/desktop/fara.csv': {'format': 'json', 'encoding': 'utf8'},
    }
})

process.crawl(FdSpider)
process.start()
# run python feed_export.py
