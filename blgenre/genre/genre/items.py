import scrapy


class GenreItem(scrapy.Item):
    parent = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()

    // *[ @ id = "mw-content-text"] / h2[3]