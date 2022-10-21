# -*- coding: utf-8 -*-
from operator import index
import scrapy
from scrapy.selector import Selector

class ChemkRaspisanieSpider(scrapy.Spider):
    name = 'raspisanie'
    allowed_domains = ['http://www.chemk.org/index.php/raspisanie']
    start_urls = ['https://rsp.chemk.org/1korp/today.htm',
                # 'https://rsp.chemk.org/3korp/today.htm',
                # 'https://rsp.chemk.org/4korp/today.htm',
                # 'https://rsp.chemk.org/5korp/today.htm',
                ]

    def start_requests(self):
        urls = [
            'https://rsp.chemk.org/1korp/today.htm'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Selector) -> None:
        # table = response.css('.MsoNormalTable tr span::text').extract()
        # yield {
        #     'table': [word for word in table]
        # }
        rows = []
        table_data = response.css('.MsoNormalTable td').extract()
        # for td in table_data:
        #     rows.append(td.text.strip())

        yield {
            'rows':table_data
        }