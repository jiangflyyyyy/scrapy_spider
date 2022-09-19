# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql
from datetime import datetime


class MyspiderPipeline:
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='921218', host='localhost', port=3306,
                                    database='djblog', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        tag_name = item['tag_name']
        tag_url = item['tag_url']
        sql = """insert into category(category_name, category_url, created_date, alias)
                  values ('{0}', '{1}', {2}, {3})
            """.format(tag_name, tag_url, 'SYSDATE()', "''")
        self.cursor.execute(sql)
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
