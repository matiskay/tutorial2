from scrapy import Spider, Request
from bcp2.items import PredioItemLoader


class AdondeVivirSpider(Spider):
    name = 'adondevivir'
    start_urls = [
        'https://www.adondevivir.com/departamentos-en-venta-q-lima.html'
    ]

    def parse(self, response):
        items = response.xpath('//h4[has-class("aviso-data-title")]/a')
        for item in items:
            url = item.xpath('./@href').extract_first(default='')
            url = response.urljoin(url)
            yield Request(url=url, callback=self.parse_predio)

    def parse_predio(self, response):
        pl = PredioItemLoader(response=response)

        pl.add_value('url', response.url)
        pl.add_xpath('name', '//h2[has-class("info-title")]')
        pl.add_xpath('address', '//h2[has-class("info-location")]')
        pl.add_xpath('description', '//div[has-class("description-container")]')
        pl.add_xpath('price', '//span[has-class("data-price")]')

        yield pl.load_item()