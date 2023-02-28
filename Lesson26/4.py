import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page1.html'

html = requests.get(url)
bs = BeautifulSoup(html.text,'html.parser')
print(bs.title.text.strip())
print(bs.div.text.strip())