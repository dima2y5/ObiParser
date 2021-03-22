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

        Rule(LinkExtractor(allow=r'shtukaturki/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'shpaklevki/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'peskobeton-alebastr-i-drugie-sukhie-rastvory/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'cement/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'vyravnivayushie-smesi/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'germetiki/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'klei-dlya-plitki/.*'), callback='parse_smesi', follow=True),
        Rule(LinkExtractor(allow=r'gipsokarton/.*'), callback='parse_derevo', follow=True),
        Rule(LinkExtractor(allow=r'drevesno-plitnye-i-pilomaterialy/.*'), callback='parse_derevo', follow=True),
        Rule(LinkExtractor(allow=r'provolochnye-gvozdi-i-shtifty/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'stalnye-gvozdi-i-shtifty/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'krovelnye-gvozdi/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'shtifty-dlya-planok-i-panelei/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'gvozdi-dlya-obivki-myagkoi-mebeli/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'skoby-i-petli/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'ankernye-gvozdi/.*'), callback='parse_kreplenia', follow=True),
        Rule(LinkExtractor(allow=r'mednye-gvozdi-i-shtifty/.*'), callback='parse_kreplenia', follow=True),
    )


    def parse_smesi(self,response):

        root = Selector(response)
        posts = root.xpath('//section[@class="overview__description span7-half"]')
        tables = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        desc = root.xpath('//div[@class="description-text js-toggle-additional-content toggle-additional-content toggle-additional-content--text-centered clearfix"]')
        price = root.xpath('//span[@class="overview__price"]')
        link = root.xpath('//link[@rel="canonical"]')
        types = root.xpath('//div[@class="table-container table-unstyled"]')
        img = root.xpath('.//img[@class="ads-slider__image jqzoom"]')
        table1 = root.xpath('//div[@class="table-container table-0 table-unstyled"]')
        table2 = root.xpath('//div[@class="table-container table-unstyled"]')
        table3 = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        availability = root.xpath('//div[@class="span6 span-tablet6"]')

        for post in posts:
            h = 'https:'
            item = ProductItem()
            item['category'] = 'Сухие смеси и грунтовки'
            item['type'] = types.xpath('.//tr[1]/td/text()').extract()[0]
            item['title'] = post.xpath('.//h1/text()').extract()[0]
            item['weight'] = tables.xpath('.//tr[1]/td/span/span/text()').extract()[0]
            item['desc'] = desc.xpath('.//p[3]/text()').extract()[0]
            item['price'] = price.xpath('.//strong/strong/text()').extract()[0]
            item['link'] = link.xpath('.//@href').extract()[0]
            item['img'] = h + img.xpath('.//@src').extract()[0]
            item['table1'] = table1.xpath('.//tbody/tr/*/text()').extract()
            item['table2'] = table2.xpath('.//tbody/tr/*/text()').extract()
            item['table3'] = table3.xpath('.//tbody/tr/*/text()').extract()
            item['availability'] = availability.xpath('.//p[@class="font-xs green"]/text()').extract()[0]

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
        table1 = root.xpath('//div[@class="table-container table-0 table-unstyled"]')
        table2 = root.xpath('//div[@class="table-container table-unstyled"]')
        table3 = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        availability = root.xpath('//div[@class="flag_body"]')


        for post in posts:
            h = 'https:'
            item = GermetikItem()
            item['category'] = 'Сухие смеси и грунтовки'
            item['type'] = 'Герметик'
            item['base'] = base.xpath('.//tr[1]/td/text()').extract()[0]
            item['title'] = post.xpath('.//h1/text()').extract()[0]
            item['weight'] = tables.xpath('.//tr[1]/td/span/span/text()').extract()[0]
            item['desc'] = desc.xpath('.//p[3]/text()').extract()[0]
            item['price'] = price.xpath('.//strong/strong/text()').extract()[0]
            item['link'] = link.xpath('.//@href').extract()[0]
            item['img'] = h + img.xpath('.//@src').extract()[0]
            item['table1'] = table1.xpath('.//tbody/tr/*/text()').extract()
            item['table2'] = table2.xpath('.//tbody/tr/*/text()').extract()
            item['table3'] = table3.xpath('.//tbody/tr/*/text()').extract()
            item['availability'] = availability.xpath('.//p[@class="font-xs green"]/text()').extract()

            yield item

    def parse_derevo(self,response):

        root = Selector(response)
        posts = root.xpath('//section[@class="overview__description span7-half"]')
        tables = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        desc = root.xpath('//div[@class="description-text js-toggle-additional-content toggle-additional-content toggle-additional-content--text-centered clearfix"]')
        price = root.xpath('//span[@class="overview__price"]')
        link = root.xpath('//link[@rel="canonical"]')
        types = root.xpath('//div[@class="table-container table-unstyled"]')
        img = root.xpath('.//img[@class="ads-slider__image jqzoom"]')
        table1 = root.xpath('//div[@class="table-container table-0 table-unstyled"]')
        table2 = root.xpath('//div[@class="table-container table-unstyled"]')
        table3 = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        availability = root.xpath('//div[@class="span6 span-tablet6"]')

        for post in posts:
            h = 'https:'
            item = ProductItem()
            item['category'] = 'Древесно-плитные и пиломатериалы'
            item['type'] = types.xpath('.//tr[1]/td/text()').extract()[0]
            item['title'] = post.xpath('.//h1/text()').extract()[0]
            item['weight'] = tables.xpath('.//tr[1]/td/span/span/text()').extract()[0]
            item['desc'] = desc.xpath('.//p[3]/text()').extract()[0]
            item['price'] = price.xpath('.//strong/strong/text()').extract()[0]
            item['link'] = link.xpath('.//@href').extract()[0]
            item['img'] = h + img.xpath('.//@src').extract()[0]
            item['table1'] = table1.xpath('.//tbody/tr/*/text()').extract()
            item['table2'] = table2.xpath('.//tbody/tr/*/text()').extract()
            item['table3'] = table3.xpath('.//tbody/tr/*/text()').extract()
            item['availability'] = availability.xpath('.//p[@class="font-xs green"]/text()').extract()[0]

            yield item

    def parse_kreplenia(self,response):

        root = Selector(response)
        posts = root.xpath('//section[@class="overview__description span7-half"]')
        tables = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        desc = root.xpath('//div[@class="description-text js-toggle-additional-content toggle-additional-content toggle-additional-content--text-centered clearfix"]')
        price = root.xpath('//span[@class="overview__price"]')
        link = root.xpath('//link[@rel="canonical"]')
        types = root.xpath('//div[@class="table-container table-unstyled"]')
        img = root.xpath('.//img[@class="ads-slider__image jqzoom"]')
        table1 = root.xpath('//div[@class="table-container table-0 table-unstyled"]')
        table2 = root.xpath('//div[@class="table-container table-unstyled"]')
        table3 = root.xpath('//div[@class="table-container table-1 table-unstyled"]')
        availability = root.xpath('//div[@class="span6 span-tablet6"]')

        for post in posts:
            h = 'https:'
            item = ProductItem()
            item['category'] = 'Крепления, гвозди и штифты'
            item['type'] = types.xpath('.//tr[1]/td/text()').extract()[0]
            item['title'] = post.xpath('.//h1/text()').extract()[0]
            item['weight'] = tables.xpath('.//tr[1]/td/span/span/text()').extract()[0]
            item['desc'] = desc.xpath('.//p[3]/text()').extract()[0]
            item['price'] = price.xpath('.//strong/strong/text()').extract()[0]
            item['link'] = link.xpath('.//@href').extract()[0]
            item['img'] = h + img.xpath('.//@src').extract()[0]
            item['table1'] = table1.xpath('.//tbody/tr/*/text()').extract()
            item['table2'] = table2.xpath('.//tbody/tr/*/text()').extract()
            item['table3'] = table3.xpath('.//tbody/tr/*/text()').extract()
            item['availability'] = availability.xpath('.//p[@class="font-xs green"]/text()').extract()[0]

            yield item

