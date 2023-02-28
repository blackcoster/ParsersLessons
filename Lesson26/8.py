import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F'
html = requests.get(url)

bs = BeautifulSoup(html.text,'html.parser')
result = bs.h1.text
print(f'Заголовок: {result}')