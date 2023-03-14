import requests
from bs4 import BeautifulSoup
import lxml

class Content:
    def __init__(self,url,title,body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print(f'URL: {self.url}')
        print(f'TITLE:  {self.title}')
        print(f'BODY:\n  {self.body}')

class Website:
    def __init__(self,name,url,titleTag,bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:
    def getPage(self,url):
        try:
            html = requests.get(url)
        except:
            return None
        return BeautifulSoup(html.text, 'lxml')

    def safeGet(self,pageObj,selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems)>0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self,site,url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs,site.titleTag)
            body = self.safeGet(bs,site.bodyTag)
            if title!=0 and body!=0:
                content = Content(url,title,body)
                content.print()

crawler = Crawler()
siteData = [
    ['Brookings','https://www.brookings.edu','h1','div.post-body']
]
websites = []
for row in siteData:
    websites.append(Website(row[0],row[1],row[2],row[3]))
crawler.parse(websites[0],
             'https://www.brookings.edu/blog/future-development/2022/03/04/how-to-close-europes-digital-divide/')
