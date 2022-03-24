import scrapy
from ..items import TestspiderItem

class QuotesSpider(scrapy.Spider):
    name = 'quotestoscrape'
    start_urls = [ 'https://quotes.toscrape.com/' ]

    def parse(self, response):

        items = TestspiderItem()

        # response.css(...)[0].extract() - returns the first value (or an error)
        # response.css(...).extract_first() - returns the first value (or a None)
        quote = response.css('span.text::text').extract()
        author = response.css('.author::text').extract()
        tag = response.css('.tag::text').extract()

        items['quote'] = quote
        items['author'] = author
        items['tag'] = tag

        yield items
