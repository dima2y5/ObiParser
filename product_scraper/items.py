FEED_EXPORT_ENCODING = 'utf-8'
import scrapy


class ProductItem(scrapy.Item):
    type = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()

class GermetikItem(scrapy.Item):
    type = scrapy.Field()
    base = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()