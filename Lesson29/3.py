import requests
from bs4 import BeautifulSoup
import re
# ссылки на одной странице
html = requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.text, 'lxml')
for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
   if 'href' in link.attrs:
       print(link.attrs['href'])

