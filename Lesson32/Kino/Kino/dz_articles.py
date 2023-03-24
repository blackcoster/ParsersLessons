from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider):
    name = 'Sonya'
    allowed_domains = ['kinopoisk.ru']
    start_urls = ['https://www.kinopoisk.ru/media/article/4007615/?from_block=editorial_choice']
    rules = [Rule(LinkExtractor(allow='/media/article'), callback='parse_items', follow=True)]

    # ЭТО ДЗ ПРОШЛОГО УРОКА
    # def parse_items(self, response):
    #     url = response.url
    #     title = response.xpath('//h1//span/text()').get()
    #     print('URL is: {}'.format(url))
    #     print('Title is: {}'.format(title))


    #ЭТО ДЗ ЭТОГО УРОКА
    def parse_items(self, response):
        url = response.url
        title = response.xpath('//h1//span/text()').get()
        yield {'URL':url,
               'TITLE':title}

