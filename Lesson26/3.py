import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Python'

html = requests.get(url)
bs = BeautifulSoup(html.text,'html.parser')

with open('python.html','w',encoding='utf-8') as file:
    file.write(str(bs))