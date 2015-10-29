# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding("utf8")

class FortuneListPipeline(object):
	def __init__(self):
		self.file=codecs.open('fortune_list.json',mode='wb',encoding='utf-8')

	def process_item(self, item, spider):
		line='the list:'+'\n'

		for i in range(len(item['name'])):
			name={'company_name':str((item['name'][i]))}
			num={'company_count':str((item['num'][i]))}
			line=line+json.dumps(name,ensure_ascii=False)
			line=line+json.dumps(num,ensure_ascii=False)
			line=line+'\n'

		self.file.write(line)

	def close_spider(self,spider):
		self.file.close()
		
