import scrapy


class Scraping(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        thought = response.css("div.quote")
        for i in thought:
           dict = {
               "quote": i.css("span.text::text").get(),
               "author": i.css("small.author::text").get(),
               "tags": i.css("a.tag::text").getall(),
               "about the author": i.css('a::attr(href)').extract()
           }
           yield dict


