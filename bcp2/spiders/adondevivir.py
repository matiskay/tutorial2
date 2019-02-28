from scrapy import Spider
from bcp2.items import PredioItemLoader


class AdondeVivirSpider(Spider):
    name = 'adondevivir'
    start_urls = [
        'https://www.adondevivir.com/propiedades/flat-petit-tower-53931295.html'
    ]

    def parse(self, response):
        pl = PredioItemLoader(response=response)

        # nl.add_xpath('title', '//h1')
        # nl.add_xpath('content', '//div[has-class("news-text-content")]/p')
        # nl.add_xpath('image', '//div[has-class("image")]//img/@src')
        # nl.add_value('url', response.url)
        #
        # yield nl.load_item()