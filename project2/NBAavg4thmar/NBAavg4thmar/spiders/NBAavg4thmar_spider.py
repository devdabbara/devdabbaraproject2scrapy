


import scrapy 
from scrapy import Spider
from scrapy.selector import Selector
from NBAavg4thmar.items import NBAavg4thmar_Item


class NBAavg4thmarSpider(Spider):
	name = 'NBAavg4thmar_spider'
	allowed_urls = ['www.teamrankings.com/']
	start_urls = ['https://www.teamrankings.com/nba/stat/average-4th-quarter-margin?date=2017-06-13']

	def parse(self, response):
		rows = response.xpath('//*[@id="html"]/body/div/div/div/main/table/tbody/tr')

		for i in range(0, 30):
			Rank = rows[i].xpath('./td[1]/text()').extract_first()
			Team = rows[i].xpath('./td[2]/a/text()').extract_first()
			_2016Season = rows[i].xpath('./td[3]/text()').extract_first()
			Last_3 = rows[i].xpath('./td[4]/text()').extract_first()
			Last_1 = rows[i].xpath('./td[5]/text()').extract_first()
			Home = rows[i].xpath('./td[6]/text()').extract_first()
			Away = rows[i].xpath('./td[7]/text()').extract_first()
			_2015Season = rows[i].xpath('./td[8]/text()').extract_first()

			item = NBAavg4thmar_Item()
			item['Rank'] = Rank
			item['Team'] = Team
			item['_2016Season'] = _2016Season
			item['Last_3'] = Last_3
			item['Last_1'] = Last_1
			item['Home'] = Home
			item['Away'] = Away
			item['_2015Season'] = _2015Season
			yield item