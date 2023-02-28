import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Python'

html = requests.get(url)
bs = BeautifulSoup(html.text,'html.parser')
print(bs.html.body.h1)
print(bs.h1.text)
# result = html.read()
# print(result)
