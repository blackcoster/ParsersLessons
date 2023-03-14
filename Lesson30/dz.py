import requests
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
   global pages
   html = requests.get(pageUrl)
   bs = BeautifulSoup(html.text, 'lxml')
   for link in bs.find_all('a'):
       if 'href' in link.attrs:
           if link.attrs['href'] not in pages:
               if 'https' in link.attrs['href']:
                   newPage = link.attrs['href']
                   print(newPage)
                   pages.add(newPage)
                   getLinks(newPage)



getLinks('https://docs.python.org/3/library/index.html')
