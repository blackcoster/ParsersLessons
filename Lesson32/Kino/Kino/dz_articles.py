from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider):
    name = 'Sonya'
    allowed_domains = ['kinopoisk.ru']
    start_urls = ['https://www.kinopoisk.ru/media/article/4007615/?from_block=editorial_choice']
    rules = [Rule(LinkExtractor(allow='/media/article'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.xpath('//h1//span/text()').get()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))

    # def parse(self, response, **kwargs):
    #         for article in response
    #         url = response.url
    #         title = response.xpath('//h1//span/text()').get()
    #         yield {
    #             'text': f'url - {url}',
    #             'title': f'title - {title}'
    #     }
