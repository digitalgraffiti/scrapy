import scrapy
from genre.items import GenreItem


class GenreSpider(scrapy.Spider):
    name = 'genre'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_writing_genres']

    def parse(self, response):
        # first we get the links from the main genre section

# Major genres
        for link in response.xpath('//*[@id="mw-content-text"]/ul[1]/li/a'):
            item = GenreItem()
            item['parent'] = response.xpath('//*[@id="mw-content-text"]/h3[1]').extract_first() #<---I give up. I just want the text. this is to be the same on every item in this particular list
            item['url'] = response.urljoin(link.xpath('@href').extract_first())
            item['name'] = link.xpath('@title').extract_first()
            yield item


# Common genres: fiction
        for link in response.xpath('//*[@id="mw-content-text"]/ul[2]/li'):
            item = GenreItem()
            item['parent'] = response.xpath('//*[@id="mw-content-text"]/h3[2]').extract_first() #<---I give up
            item['url'] = response.urljoin(link.xpath('a/@href').extract_first())
            item['name'] = link.xpath('a/@title').extract_first()# some of these dont have links and it mucks stuff up
            item['desc'] = link.xpath('text()').extract_first()# the name ends up here with gibberish characters between it and the desc
            yield item


# Common genres: nonfiction
        for link in response.xpath('//*[@id="mw-content-text"]/ul[3]/li'):
            item = GenreItem()
            item['parent'] = response.xpath('//*[@id="mw-content-text"]/h3[3]').extract_first() #<---I give up
            item['url'] = response.urljoin(link.xpath('a/@href').extract_first())
            item['name'] = link.xpath('a/@title').extract_first()
            item['desc'] = link.xpath('text()').extract_first()
            yield item


# Genres and subgenres
        for link in response.xpath('//*[@id="mw-content-text"]/ul[3]/li'):# ther are lots and lots of sub-lists
            item = GenreItem()
            item['parent'] = response.xpath('//*[@id="mw-content-text"]/h2[3]').extract_first() #<---I give up
            item['url'] = response.urljoin(link.xpath('a/@href').extract_first())
            item['name'] = link.xpath('a/@title').extract_first()
            item['desc'] = link.xpath('text()').extract_first()
            yield item