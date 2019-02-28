from scrapy import Spider, Request
from bcp2.items import PredioItemLoader

from w3lib.html import remove_tags
from bcp2.utils import calculate_total_of_pages


class AdondeVivirSpider(Spider):
    name = 'adondevivir'
    start_urls = [
        'https://www.adondevivir.com/departamentos-en-venta-q-lima.html'
    ]

    def parse(self, response):

        for r in self.parse_predios(response):
            yield r

        total = response.xpath('//h1[has-class("resultado-title")]/strong').extract_first(default='')
        total = remove_tags(total)
        total = total.replace(',', '')
        total = int(total)

        pages = calculate_total_of_pages(total, 25)

        for page in range(2, pages + 1):
            url = 'https://www.adondevivir.com/departamentos-en-venta-pagina-{}-q-lima.html'.format(page)
            yield Request(url=url, callback=self.parse_predios)

    def parse_predios(self, response):
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