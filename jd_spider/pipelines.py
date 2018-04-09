# -*- coding: utf-8 -*-

import MySQLdb.cursors
from twisted.enterprise import adbapi

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy import log

SETTINGS = get_project_settings()


class MySQLPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        # Instantiate DB
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host=SETTINGS['DB_HOST'],
                                            user=SETTINGS['DB_USER'],
                                            passwd=SETTINGS['DB_PASSWD'],
                                            port=SETTINGS['DB_PORT'],
                                            db=SETTINGS['DB_DB'],
                                            charset='utf8',
                                            use_unicode=True,
                                            cursorclass=MySQLdb.cursors.DictCursor
                                            )
        self.stats = stats
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        """ Cleanup function, called after crawing has finished to close open
            objects.
            Close ConnectionPool. """
        self.dbpool.close()

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._insert_record, item)
        query.addErrback(self._handle_error)
        return item

    def _insert_record(self, tx, item):
        ID = item['ID'][0].encode('utf-8')
        name = item['name'][0].encode('utf-8')
        link = item['link'][0].encode('utf-8')
        price = item['price'][0].encode('utf-8')
        battery = item['battery'][0].encode('utf-8')
        frontResol = item['frontResol'][0].encode('utf-8')
        backResol = item['backResol'][0].encode('utf-8')
        color = item['color'][0].encode('utf-8')
        rom = item['rom'][0].encode('utf-8')

        sql = "INSERT INTO jd_goods VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (ID, name, link, price, color, frontResol, backResol, rom, battery)
        tx.execute(sql)
        print "Crawling"

    def _handle_error(self, e):
        log.err(e)



