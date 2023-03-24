# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class KinoPipeline:
    def process_item(self, item, spider):
        return item


# from items import Article
# from string import whitespace
#
#
# class KinoPipeline(object):
#    def process_item(self, article, spider):
#        article['text'] = [line for line in article['text'] if line not in whitespace]
#        article['text'] = ''.join(article['text'])
#        return article
