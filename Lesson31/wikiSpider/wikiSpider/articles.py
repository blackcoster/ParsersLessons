from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from items import Article

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'),callback='parse_items',follow = True)]

    def parse_items(self,response):
        article = Article()
        article['url']=response.url
        article['title'] = response.css('[class="mw-page-title-main"]::text').extracts()
        return article


