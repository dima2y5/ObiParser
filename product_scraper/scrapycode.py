import scrapy
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items import ProductItem
from items import GermetikItem


class OBISpyder(CrawlSpider):

    name = 'obi_spyder'
    allowed_domains = ['obi.ru']
    start_urls = ['https://www.obi.ru']


    rules = (

        Rule(LinkExtractor(allow=r'shtukaturki/.*'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'shpaklevki/.*'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'peskobeton-alebastr-i-drugie-sukhie-rastvory/.*'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'cement/.*'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'vyravnivayushie-smesi/.*'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'metallicheskie-setki-i-armatura/.*'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'germetiki/.*'), callback='parse_germetik', follow=True),
        Rule(LinkExtractor(allow=r'klei-dlya-plitki/.*'), callback='parse_product', follow=True),
    )


    def parse_product(self,response):
        root = Selector(response)
        posts = root.xpath('//section[@class="overview__description span7-half"]')
        tables = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        desc = root.xpath('//div[@class="description-text js-toggle-additional-content toggle-additional-content toggle-additional-content--text-centered clearfix"]')
        price = root.xpath('//span[@class="overview__price"]')
        link = root.xpath('//link[@rel="canonical"]')
        types = root.xpath('//div[@class="table-container table-unstyled"]')
        img = root.xpath('.//img[@class="ads-slider__image jqzoom"]')

        for post in posts:
            h = 'https:'
            item = ProductItem()
            item['type'] = types.xpath('.//tr[1]/td/text()').extract()[0]
            item['title'] = post.xpath('.//h1/text()').extract()[0]
            item['weight'] = tables.xpath('.//tr[1]/td/span/span/text()').extract()[0]
            item['desc'] = desc.xpath('.//p[3]/text()').extract()[0]
            item['price'] = price.xpath('.//strong/strong/text()').extract()[0]
            item['link'] = link.xpath('.//@href').extract()[0]
            item['img'] = h + img.xpath('.//@src').extract()[0]
            yield item

    def parse_germetik(self,response):
        root = Selector(response)
        posts = root.xpath('//section[@class="overview__description span7-half"]')
        tables = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        desc = root.xpath('//div[@class="description-text js-toggle-additional-content toggle-additional-content toggle-additional-content--text-centered clearfix"]')
        price = root.xpath('//span[@class="overview__price"]')
        link = root.xpath('//link[@rel="canonical"]')
        base = root.xpath('//div[@class="table-container table-unstyled"]')
        img = root.xpath('.//img[@class="ads-slider__image jqzoom"]')

        for post in posts:
            h = 'https:'
            item = GermetikItem()
            item['type'] = 'Герметик'
            item['base'] = base.xpath('.//tr[1]/td/text()').extract()[0]
            item['title'] = post.xpath('.//h1/text()').extract()[0]
            item['weight'] = tables.xpath('.//tr[1]/td/span/span/text()').extract()[0]
            item['desc'] = desc.xpath('.//p[3]/text()').extract()[0]
            item['price'] = price.xpath('.//strong/strong/text()').extract()[0]
            item['link'] = link.xpath('.//@href').extract()[0]
            item['img'] = h + img.xpath('.//@src').extract()[0]
            yield item