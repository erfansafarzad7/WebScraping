import scrapy
from ..items import SItem


class FaraSpider(scrapy.Spider):
    name = "fara"
    allowed_domains = ["www.faradars.org"]
    start_urls = ["https://faradars.org/how-to-learn/programming"]

    def parse(self, response, **kwargs):
        items = SItem()
        image_urls = []

        for fara in response.css('div.flex-wrap:nth-child(3)'):
            img_url = fara.css('img').attrib['src']
            image_urls.append(img_url)
        items['file_urls'] = image_urls
        yield items
