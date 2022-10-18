# -*- coding: utf-8 -*-
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
        table = response.css('.MsoNormalTable tr span::text').getall()
        for text in table:
            yield {
                'table':text
                }
        # for span in response.xpath('//tr/td/p'):
            # yield {
            #     'gruppa': span.xpath("//span[0][contains(@style,'font-size:9.0pt;mso-fareast-language:RU')]//text()").getall(),
            #     'Para': span.xpath("//span[1][contains(@style,'font-size:9.0pt;mso-fareast-language:RU')]//text()").getall(),
            #     'Zamena': span.xpath("//span[2][contains(@style,'font-size:9.0pt;mso-fareast-language:RU')]//text()").getall(),
            # }