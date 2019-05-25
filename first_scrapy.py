import scrapy


class MyFirstSpider(scrapy.Spider):
    name = "my-first-spyder"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/'
        ]
        requests = []
        for url in urls:
            requests.append(
                scrapy.Request(url=url, callback=self.parse)
            )

        return requests

    def parse(self, response):
        self.logger.info(
            'Just Parsing {}'.format(response.url)
        )
