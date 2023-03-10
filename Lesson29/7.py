from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import re
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

pages = set()

#

# Получить список всех внутренних ссылок, найденных на странице.
def getInternalLinks(bs, includeUrl):
   includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
   internalLinks = []
   # найти все ссылки, которые начинаются с "/"
   for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
       if link.attrs['href'] is not None:
           if link.attrs['href'] not in internalLinks:
               if (link.attrs['href'].startswith('/')):
                   internalLinks.append(includeUrl + link.attrs['href'])
           else:
               internalLinks.append(link.attrs['href'])
   return internalLinks


# Получить список всех внешних ссылок, найденных на странице.
def getExternalLinks(bs, excludeUrl):
   externalLinks = []
   # Найти все ссылки, которые начинаются с "http" или "www",
   # не содержащие текущий URL.
   for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
       if link.attrs['href'] is not None:
           if link.attrs['href'] not in externalLinks:
               externalLinks.append(link.attrs['href'])
   return externalLinks

def getRandomExternalLink(startingPage):
   html = urlopen(startingPage)
   bs = BeautifulSoup(html, 'html.parser')
   externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
   if len(externalLinks) == 0:
       print('No external links, looking around the site for one')
       domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
       internalLinks = getInternalLinks(bs, domain)
       return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
   else:
       return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
   externalLink = getRandomExternalLink(startingSite)
   print('Random external link is:{}'.format(externalLink))
   followExternalOnly(externalLink)


followExternalOnly('https://www.labirint.ru/')
