# -*- coding: utf-8 -*-

# Scrapy settings for jd_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'

COOKIES_ENABLED = False
#DOWNLOAD_DELAY = 0.1  
LOG_LEVEL = 'INFO'
DB_HOST = 'localhost'
DB_PORT = '' 
DB_USER = ''
DB_PASSWD = '' #请重新配置数据库的信息
DB_DB = ''

ITEM_PIPELINES = {
    'jd_spider.pipelines.MySQLPipeline': 300,  
}
