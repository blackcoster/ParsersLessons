from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import _thread
import time


def get_links(thread_name, bs):
   print('Getting links in{}'.format(thread_name))
   return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


# Определяем функцию для потока
def scrape_article(thread_name, path):
   html = urlopen('http://en.wikipedia.org{}'.format(path))
   time.sleep(5)
   bs = BeautifulSoup(html, 'html.parser')
   title = bs.find('h1').get_text()
   print('Scraping {} in thread{}'.format(title, thread_name))
   links = get_links(thread_name, bs)
   if len(links) > 0:
       newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
       print(newArticle)
       scrape_article(thread_name, newArticle)


# Создаем следующие два потока:
try:
   _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon',))
   _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python',))
except:
   print('Error: unable to start threads')
while 1:
   pass



