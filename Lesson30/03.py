import requests
from bs4 import BeautifulSoup


class Content:
   def __init__(self, topic, url, title, body):
       self.topic = topic
       self.url = url
       self.title = title
       self.body = body

   def print(self):
       print(f'Новая тема {self.topic}')
       print(f'URL {self.url}')
       print(f'Заголовок {self.title}')
       print(f'Содержимое \n{self.body}')


class Website:
   def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
       self.name = name
       self.url = url
       self.searchUrl = searchUrl
       self.resultListing = resultListing
       self.resultUrl = resultUrl
       self.absoluteUrl = absoluteUrl
       self.titleTag = titleTag
       self.bodyTag = bodyTag


class Crawler:
   def getPage(self, url):
       try:
           r = requests.get(url)
       except requests.exceptions.RequestException:
           return None
       return BeautifulSoup(r.text, 'lxml')

   def safeGet(self, pageObj, selector):
       selectedItem = pageObj.select(selector)

       if selectedItem is not None and len(selectedItem) > 0:
           return selectedItem[0].get_text()
       return ''

   def search(self, topic, site):
       bs = self.getPage(site.searchUrl + topic)
       searchResults = bs.select(site.resultListing)
       for result in searchResults:
           url = result.select(site.resultUrl)[0].attrs['href']
           if (site.absoluteUrl):
               bs = self.getPage(url)
           else:
               bs = self.getPage(site.url + url)
           if bs is None:
               print('Ошибка')
               return
           title = self.safeGet(bs, site.titleTag)
           body = self.safeGet(bs, site.bodyTag)
           if title != '' and body != '':
               content = Content(topic, title, body, url)
               content.print()
           else:
               return


crawler = Crawler()
class Website:
   def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
       self.name = name
       self.url = url
       self.searchUrl = searchUrl
       self.resultListing = resultListing
       self.resultUrl = resultUrl
       self.absoluteUrl = absoluteUrl
       self.titleTag = titleTag
       self.bodyTag = bodyTag

siteData = [
   ['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=', 'div.list-content article',
    'h4.title a', True, 'h1', 'div.post-body']

]
websites = []
for row in siteData:
   websites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

topics = ['Python']
for topic in topics:
   print(f'Информация по теме {topic}')
   for targetSite in websites:
       crawler.search(topic, targetSite)
