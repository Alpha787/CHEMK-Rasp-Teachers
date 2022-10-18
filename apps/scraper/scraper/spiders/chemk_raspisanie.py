# -*- coding: utf-8 -*-
import scrapy


class ChemkRaspisanieSpider(scrapy.Spider):
    name = 'raspisanie'
    allowed_domains = ['http://www.chemk.org/index.php/raspisanie']
    start_urls = ['https://rsp.chemk.org/1korp/today.htm']

    def parse(self, response):
        for subject in response.xpath('//tr/td/p'):
            yield {
                'text': subject.xpath("//span[contains(@style,'font-size:9.0pt;mso-fareast-language:RU')]//text()").getall()
            }
