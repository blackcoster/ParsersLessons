import requests
from bs4 import BeautifulSoup
import re

pages = set()
# сбор данных внутри всех страниц

def getLinks(pageUrl):
   global pages
   html = requests.get(f'http://en.wikipedia.org{pageUrl}')
   bs = BeautifulSoup(html.text, 'lxml')
   for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
       if 'href' in link.attrs:
           if link.attrs['href'] not in pages:
               newPage = link.attrs['href']
               print(newPage)
               pages.add(newPage)
               getLinks(newPage)


getLinks('')
