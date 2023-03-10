import requests
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
   global pages
   html = requests.get("http://en.wikipedia.org" + pageUrl)
   bs = BeautifulSoup(html.text, 'lxml')
   try:
       print(bs.h1.get_text())
       print(bs.find(id="mw-content-text").findAll("p")[0].text)
   except AttributeError:
       print("На этой странице чего-то не хватает!")

   for link in bs.findAll("a", href=re.compile("^(/wiki/)")):
       if 'href' in link.attrs:
           if link.attrs['href'] not in pages and '/wiki/Special' not in link.attrs['href']:
               newPage = link.attrs['href']
               print("----------------\n" + newPage)
               pages.add(newPage)
               getLinks(newPage)


getLinks("")
