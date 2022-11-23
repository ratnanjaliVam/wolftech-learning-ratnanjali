import scrapy


class Scraping(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):

        quotename = response.css('span.text::text').getall()
        yield {'titletext': quotename}

