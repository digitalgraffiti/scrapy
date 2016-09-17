import scrapy


class GenreSpider(scrapy.Spider):
    name = "genre"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_writing_genres',
    ]

    def parse(self, response):
        for genre in response.xpath('//ul/li'):
            gname = genre.xpath('//ul/li/a/text()').extract_first()
            glink = genre.xpath('//ul/li/a').extract_first()
            gdesc = genre.xpath('//ul/li/text()').extract_first()
            print(u'{}: {}'.format(gname, glink, gdesc))

