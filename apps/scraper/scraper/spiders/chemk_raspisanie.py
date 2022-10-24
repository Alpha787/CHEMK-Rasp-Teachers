# -*- coding: utf-8 -*-
from operator import index
import scrapy
from scrapy.selector import Selector
import re

# FIXME: здесь 
class ChemkRaspisanieSpider(scrapy.Spider):
    name = 'raspisanie'
    allowed_domains = ['http://www.chemk.org/index.php/raspisanie']
    start_urls = ['https://rsp.chemk.org/1korp/tomorrow.htm',
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
        table = response.css('.MsoNormalTable tr').extract()
        body = table.css('tr').getall()
        head = body[0]
        body_rows = body[2:]

        headings = []
        for item in head.contents:
            item = (item.text).rstrip("\n")
            headings.append(item)

        all_rows = []
        for row_num in range(len(body_rows)):
            row = []
            for row_item in body_rows[row_num].css("td").getall():
                aa = re.sub("(\xa0)|(\n)", "", "", row_item.text)
                row.append(aa)
            all_rows.append(row)

        print(all_rows[0:30][0:6])




        # rows = []
        # table_data = response.css('.MsoNormalTable td').extract()
        # for td in table_data:
        #     rows.append(td.text.strip())

        # yield {
        #     'rows':table_data
        # }