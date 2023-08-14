from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MatalanSpider(CrawlSpider):
    name = 'matalan'
    allowed_domains = ['www.matalan.co.uk', ]
    start_urls = [
        'https://www.matalan.co.uk/mens/suits.list',
    ]

    rules = [
        Rule(LinkExtractor(allow=r'/product/detail/'), callback='get_pid', follow=False)
    ]

    def get_pid(self, response):
        item = {}
        item['p_id'] = response.css('div.sc-LoTwT:nth-child(2) > div:nth-child(2)::text').get()
        return item
