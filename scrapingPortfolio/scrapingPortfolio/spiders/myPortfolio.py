import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'myPortfolio'
    allowed_domains = ['ratnanjali.codes']
    start_urls = ['https://ratnanjali.codes/']

    def parse(self, response):
        projects = response.css("div.ml-4")
        for i in projects:
            project_names = i.css("h2::text").get()
            yield project_names
