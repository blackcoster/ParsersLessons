import requests
from bs4 import BeautifulSoup
import lxml

BASE_URL = 'https://habr.com'

def get_url(url:str):
    r = requests.get(url)
    if not r.raise_for_status():
        bs = BeautifulSoup(r.text, 'lxml')
        url_list = bs.find_all('a', class_="tm-article-snippet__title-link")
        for i in range(len(url_list)):
            url_list[i] = BASE_URL + url_list[i].get('href')
        return url_list

def get_content(url):
    r = requests.get(url)
    if not r.raise_for_status():
        bs = BeautifulSoup(r.text, 'lxml')
        title_article = bs.h1.text
        content_article = bs.find('div',id='post-content-body').text
        return f'{url}\n{title_article}\n{content_article}\n_______________\n'

links = get_url('https://habr.com')
if len(links) > 0:
    for link in links:
        article = get_content(link)
        print(article)
