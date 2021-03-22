FEED_EXPORT_ENCODING = 'utf-8'
import scrapy


class ProductItem(scrapy.Item):
    category = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    table1 = scrapy.Field()
    table2 = scrapy.Field()
    table3 = scrapy.Field()
    availability = scrapy.Field()

class GermetikItem(scrapy.Item):
    category = scrapy.Field()
    type = scrapy.Field()
    base = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    table1 = scrapy.Field()
    table2 = scrapy.Field()
    table3 = scrapy.Field()
    availability = scrapy.Field()