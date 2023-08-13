import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://fa.wikipedia.org/wiki/%D8%A8%D8%B1%D9%88%D8%B3_%D9%84%DB%8C',
                 'https://en.wikipedia.org/wiki/Genghis_Khan']

    def parse(self, response, **kwargs):
        title = response.css('title').extract()
        yield {'title': title}
