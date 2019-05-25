import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')

        for quote in quotes:
            yield {
                'quote': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'url detail page':
                    quote.css('a::attr(href)').extract_first(),
                'tags': quote.css('.tag::text').getall()

            }
