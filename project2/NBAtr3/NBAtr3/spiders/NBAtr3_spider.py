# name: an attribute specifying a unique name to identify the spider
# start_urls: an attribute listing the URLs the spider will start from
# parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data
import scrapy 
from scrapy import Spider
from scrapy.selector import Selector
from NBAtr3.items import NBAtr3_Item


class NBAtr3Spider(Spider):
	name = 'NBAtr3_spider'
	allowed_urls = ['www.teamrankings.com/']
	start_urls = ['https://www.teamrankings.com/nba/stat/points-from-3-pointers?date=2017-06-13']

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

			item = NBAtr3_Item()
			item['Rank'] = Rank
			item['Team'] = Team
			item['_2016Season'] = _2016Season
			item['Last_3'] = Last_3
			item['Last_1'] = Last_1
			item['Home'] = Home
			item['Away'] = Away
			item['_2015Season'] = _2015Season
			yield item

