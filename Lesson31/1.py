import requests
from bs4 import BeautifulSoup

import re
class Website:
    def __init__(self,name,url,targetPattern,absoluteUrl,titleTag,bodyTag):
        self.name = name
        self.url = url
        self.targetPattern  = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def printContent(self):
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))

class Crawler:
    def __init__(self,site):
        self.site = site
        self.visited = []

    def getPage(self,url):
        try:
            html = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(html.text,'html.parser')

    def safeGet(self,bs,selector):
        selectedItems = bs.select(selector)
        if selectedItems is not None and len(selectedItems)>0:
            return '\n'.join([elem.get_text() for elem in selectedItems])
        return ''

    def parse(self,url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs,self.site.titleTag)
            body = self.safeGet(bs,self.site.bodyTag)
            if title!='' and body!='':
                content = Content(url,title,body)
                content.printContent()


    def crawl(self):
        bs = self.getPage(self.site.url)
        targetPages = bs.findAll('a',href = re.compile(self.site.targetPattern))
        print(targetPages)
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = f'{self.site.url}{targetPage}'
                self.parse(targetPage)



reuters = Website('Reuters','https://www.reuters.com','^(/business/)',False,'h1','div.media-story-card__body__3tRWy')
crawler = Crawler(reuters)
crawler.crawl()



