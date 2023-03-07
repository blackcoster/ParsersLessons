import requests
import lxml
from bs4 import BeautifulSoup

url1 = 'https://www.kinopoisk.ru'
url2 = '/media/article/4007433/'
html = requests.get(url1+url2)
if not html.raise_for_status():
    bs= BeautifulSoup(html.text,'lxml')
    bs.a.get('href')

    content = bs.find('div',{'class':'media-post-setka-inner-html'})
    list_films = content.find_all('div',{'class':'stk-grid stk-theme_27251__mb_cus_72'})
    film1 = list_films[3]
    title = film1.h2.get_text()
    opisanie = film1.find('p',{'class':'stk-reset stk-theme_27251__mb_cus_36'}).text
    ssilka = url1+film1.a.get('href')
    image = film1.img.get('src')

    print(title)
    print(opisanie)
    print(ssilka)
    print(image)
