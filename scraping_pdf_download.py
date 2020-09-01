# load libraries
from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from urllib import request

class pdfItem(Item):
    reg_num = Field()
    link_pdf = Field()

class pdfCrawler(CrawlSpider):
    name = "RegistroOficial"
    # desde octubre 2007
    start_urls = ['https://www.registroficial.gob.ec/index.php/publicaciones/monthlyarchive/03/2009/limit,50']
    allowed_domains = ['www.registroficial.gob.ec']

    rules = (
        Rule(LinkExtractor(allow=r'/03/2009')),
        Rule(LinkExtractor(allow=r'/item'), callback = 'parse_items')
    )

    def parse_items(self, response):
        item = ItemLoader(pdfItem(), response)
        item.add_xpath('reg_num', '//*[@id="k2Container"]/div[1]/div/div[1]/div/div[2]/div/ul/li/div/a/@title')
        item.add_xpath('link_pdf', '//*[@id="k2Container"]/div[1]/div/div[1]/div/div[2]/div/ul/li/div/a/@href')

        yield item.load_item()

