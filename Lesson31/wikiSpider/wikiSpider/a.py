from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class ArticleSpider(CrawlSpider):
    name = 'Sonya'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('[class="mw-page-title-main"]::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
