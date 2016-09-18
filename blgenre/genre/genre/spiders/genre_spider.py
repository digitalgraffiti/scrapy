import scrapy
from genre.items import GenreItem


class GenreSpider(scrapy.Spider):
    name = 'genres-wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_writing_genres']

    def parse(self, response):
        # first we get the links from the main genre section
        links = response.xpath('//*[@id="mw-content-text"]/ul[1]/li/a')
        for link in links:
            item = GenreItem()
            item['url'] = response.urljoin(link.xpath('@href').extract_first())
            item['name'] = link.xpath('@title').extract_first()
            yield item

