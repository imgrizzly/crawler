# _*_ encoding:utf-8 _*_

import scrapy

from smallcrawler.items import SmallcrawlerItem


class QuotesSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]

    def start_requests(self):
        for i in range(2):
            start = i * 25
            url = "https://movie.douban.com/top250?start=" + str(start) + "&filter="
            yield self.make_requests_from_url(url)

    def parse(self, response):
        movies = response.xpath("//body/div/div/div/div/ol/li")

        for movie in movies:
            url = movie.xpath("div/div/div/a//@href").extract()[0]
            yield scrapy.Request(url, callback=self.get_filminfo)

    def get_filminfo(self, response):
        item = SmallcrawlerItem()
        item["filmname"] = response.css('span[property="v:itemreviewed"]::text').extract()
        item["director"] = response.css('a[rel="v:directedBy"]::text').extract()
        item["performer"] = response.css('a[rel="v:starring"]::text').extract()
        item["imdb"] = response.css('a[href^="http://www.imdb.com/"]::attr(href)').extract_first()
        item["release_time"] = response.css('span[property="v:initialReleaseDate"]::text').extract()
        item["language"] = [i.strip() for i in response.xpath('//*[@id="info"]/text()').extract_first() if u"语" in i]
        # item["language"] = [i.strip() for i in response.xpath('//*[@id="info"]').extract() if u"语言" in i][0]
        synopsis = response.xpath("//*[@id='link-report']/span[1]")[0]
        item["synopsis"] = synopsis.xpath('string(.)').extract_first().strip('\n')
        return item
