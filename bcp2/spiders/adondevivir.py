from scrapy import Spider
from bcp2.items import PredioItemLoader


class AdondeVivirSpider(Spider):
    name = 'adondevivir'
    start_urls = [
        'https://www.adondevivir.com/propiedades/flat-petit-tower-53931295.html'
    ]

    def parse(self, response):
        pl = PredioItemLoader(response=response)

        pl.add_value('url', response.url)
        pl.add_xpath('name', '//h2[has-class("info-title")]')
        pl.add_xpath('address', '//h2[has-class("info-location")]')
        pl.add_xpath('description', '//div[has-class("description-container")]')
        pl.add_xpath('price', '//span[has-class("data-price")]')

        yield pl.load_item()