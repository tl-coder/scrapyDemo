# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time

class FirstScrapyproPipeline:
    def __init__(self):
        self.fp=None

    def open_spider(self,spider):
        print('创建文件')
        self.fp=open( './'+str(time.time())+'_info.csv','w',encoding='utf8')

    def process_item(self, item, spider):
        print('kai开始写入',item['info'])
        self.fp.write(item['info']+'\n')
        return item

    def close_spider(self,spider):
        print('关闭')
        self.fp.close()