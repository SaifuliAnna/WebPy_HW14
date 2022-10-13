import scrapy


class AuthorItem(scrapy.Item):
    auther = scrapy.Field()
    quote = scrapy.Field()
    about = scrapy.Field()


class KeywordItem(scrapy.Item):
    keywords = scrapy.Field()


class DetailsItem(scrapy.Item):
    title = scrapy.Field()
    born_date = scrapy.Field()
    born_year = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()