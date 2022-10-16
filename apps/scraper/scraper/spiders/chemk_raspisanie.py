# -*- coding: utf-8 -*-
import scrapy


class ChemkRaspisanieSpider(scrapy.Spider):
    name = 'chemk_raspisanie'
    allowed_domains = ['http://www.chemk.org/index.php/raspisanie']
    start_urls = ['http://http://www.chemk.org/index.php/raspisanie/']

    def parse(self, response):
        pass
