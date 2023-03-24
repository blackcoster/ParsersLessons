from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from items import Article

class ArticleSpider(CrawlSpider):
    name = 'articlePipeline'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),callback='parse_items',follow=True)]

    def parse_items(self,response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('[class="mw-page-title-main"]::text').extract_first()
        # article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        return article