# -*- coding: utf-8 -*-
import scrapy


class ChemkRaspisanieSpider(scrapy.Spider):
    name = 'raspisanie'
    allowed_domains = ['http://www.chemk.org/index.php/raspisanie']
    start_urls = ['https://rsp.chemk.org/1korp/today.htm']

    def parse(self, response):
        page = response.url.split("/")[2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
