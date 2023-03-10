import requests
from bs4 import BeautifulSoup
import lxml

BASE_URL = 'https://habr.com'
URL = f'{BASE_URL}/ru/all/page1/'
r = requests.get(URL)
if not r.raise_for_status():
    bs = BeautifulSoup(r.text,'lxml')
    url_list = bs.find_all('a',class_ = "tm-article-snippet__title-link")
    for i in range(len(url_list)):
        url_list[i]=BASE_URL+url_list[i].get('href')
        print(url_list[i])

