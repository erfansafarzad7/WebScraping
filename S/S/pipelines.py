# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from scrapy.exceptions import DropItem


class SPipeline:
    def __init__(self):
        self.con = sqlite3.connect('countries.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS countries(
        name TEXT PRIMARY KEY, capital TEXT, population INTEGER
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""
        INSERT OR IGNORE INTO countries VALUES (?, ?, ?)
        """, (item['name'], item['capital'], item['population']))
        self.con.commit()
        return item


class PopulationPipeline:
    def process_item(self, item, spider):
        if int(item['population']) < 50_000_000:
            raise DropItem('Population is less than 50M..')
        return item
