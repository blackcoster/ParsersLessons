from pathlib import Path

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from items import Article

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/page/1/']

    # start_urls = ['https://quotes.toscrape.com/page/1/',
    #               'https://quotes.toscrape.com/page/2/']

    # def start_requests(self):
    #     urls = ['https://quotes.toscrape.com/page/1/',
    #             'https://quotes.toscrape.com/page/2/']
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    # def parse(self, response, **kwargs):
    #     page = response.url.split('/')[-2]
    #     filename = f'quotes-{page}.html'
    #     Path(filename).write_bytes(response.body)
    #     self.log(f'созраняем {filename}')

    # def parse(self, response, **kwargs):
    #     for quote in response.css('div.quote'):
    #         print({
    #             'text':quote.css("span.text::text").extract_first(),
    #             'author':quote.css("small.author::text").extract_first(),
    #             'tags':quote.css("div.tags > a.tag::text ").extract()
    #         })

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield{
                'text':quote.css("span.text::text").extract_first(),
                'author':quote.css("small.author::text").extract_first(),
                'tags':quote.css("div.tags > a.tag::text ").extract()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
