# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from fortune_list.items import FortuneListItem

class FortuneSpider(Spider):
	name="fortune_spider"

#	allowed_domains=[]

	start_urls=[
		'http://www.fortunechina.com/fortune500/c/2015-07/22/content_244442.htm'
	]

	def parse(self,response):
		sel=Selector(response)

		name=sel.xpath("//td[@class='f500c2']/a/text()").extract()
		num=sel.xpath("//td[@class='f500c6']/text()").extract()

		item=FortuneListItem()

		item['name']=[n.encode("utf-8") for n in name]
		item['num']=[n for n in num]

		yield item 

		print name