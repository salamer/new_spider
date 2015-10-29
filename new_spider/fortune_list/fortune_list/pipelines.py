# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys
import pymongo

reload(sys)
sys.setdefaultencoding("utf8")

class FortuneListPipeline(object):
    def __init__(self):
        self.mongo_url='localhost'
        self.mongo_port=27017
        self.collection_name='the_fortune_list'
        self.db_name='the_fortune_list'

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_url,self.mongo_port)
        self.db=self.client[self.db_name]
        self.con=self.db[self.collection_name]

    def close_spider(self,spider):
            self.client.close()
    def process_item(self,item,spider):
    	for i in range(len(item['name'])):
    		self.con.insert_one({"company_name":item['name'][i],"company_count":item['num'][i]})	
    		the_name=unicode(item['name'])
    		print the_name
'''	
	def __init__(self):
		self.file=codecs.open('fortune_list_debt.json',mode='wb',encoding='utf-8')

	def process_item(self, item, spider):
		line=u'the list_debt:'+'\n'


		for i in range(len(item['name'])):
			name={'company_name':str((item['name'][i]))}
			num={'company_count':str((item['num'][i]))}
			line=line+json.dumps(name,ensure_ascii=False)
			line=line+json.dumps(num,ensure_ascii=False)
			line=line+'\n'

		self.file.write(line)

	def close_spider(self,spider):
		self.file.close()
'''
