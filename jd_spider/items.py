# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class goodsItem(Item):
    link = Field()  
    ID = Field()  
    name = Field()  #手机名称
    price = Field()  #价格
    color = Field()	#颜色
    frontResol = Field() #前置摄像头像素
    backResol = Field() #后置摄像头像素
    rom = Field() #运行内存
    battery = Field()	#电池
