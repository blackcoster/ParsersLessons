import requests
from bs4 import BeautifulSoup
import datetime
import random
import re
# рандом переход по ссылкам разных страниц

def getLinks(articleUrl):
   html = requests.get(f'http://en.wikipedia.org{articleUrl}')
   bs = BeautifulSoup(html.text, 'lxml')
   return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
   newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
   print(newArticle)
   links = getLinks(newArticle)
