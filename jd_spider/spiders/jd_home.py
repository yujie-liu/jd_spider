# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from jd_spider.items import goodsItem
from scrapy.selector import Selector
import scrapy
import re
import json


class jd_spider(Spider):
    name = "jd"
    start_urls = []
    for i in range(1, 11):  # The search range is now hardwired into the program
		url = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_15127&page=' + str(i)
		start_urls.append(url)

    def parse_price(self, response):
		item1 = response.meta['item']
		temp1 = response.body.split('jQuery([')
		s = temp1[1][:-4]  # get json content
		js = json.loads(str(s))  
		if js.has_key('pcp'):
		    item1['price'] = js['pcp']
		else:
		    item1['price'] = js['p']
		return item1

    def parse_detail(self, response):
        item1 = response.meta['item']
        sel = Selector(response)
        num = item1['ID']  # retrieve the item ID
        s1 = str(num)
        color_path = "//div[@id='choose-attrs']/div[@id='choose-attr-1']/div[@class='dd']//a/i/text()"
        attr_path = "//div[@id='detail']/div[@class='tab-con']//li/text()"
        color = response.xpath(color_path).extract()
        if color:
                item1['color'] = color
        attr_list = response.xpath(attr_path).extract()
        for attr in attr_list:
			if u'电池' in attr:
				item1['battery'] = attr.split(u'：')[1]
			if u'前置' in attr:
				item1['frontResol'] = attr.split(u'：')[1]
			if u'后置' in attr:
				item1['backResol'] = attr.split(u'：')[1]
			if u'运行内存' in attr:
				item1['rom'] = attr.split(u'：')[1]
        url = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + s1[3:-2] + "&origin=2"
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_price)

    def parse(self, response):  
        goods = response.xpath('//li[@class="gl-item"]')
        for good in goods:
            item1 = goodsItem()
            item1['color'] = ['']
            item1['frontResol'] = ['']
            item1['backResol'] = ['']
            item1['rom'] = ['']
            item1['price'] = ['']
            item1['battery'] = ['']
            item1['ID'] = good.xpath('./div/@data-sku').extract()
            item1['name'] = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            item1['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()
            url = "http:" + item1['link'][0]
            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_detail)
