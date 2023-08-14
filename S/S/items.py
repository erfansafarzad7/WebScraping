import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst, MapCompose


def to_strip(value):
    return value.strip()


def to_upper(value):
    return value.upper()


class SItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, to_strip, to_upper), output_processor=TakeFirst())
    capital = scrapy.Field(input_processor=MapCompose(remove_tags, to_strip), output_processor=TakeFirst())
    population = scrapy.Field(output_processor=TakeFirst())

    file_urls = scrapy.Field()
    files = scrapy.Field()
