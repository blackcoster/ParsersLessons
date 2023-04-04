from zipfile import ZipFile
import json
import time
import lxml
import requests
import csv
import datetime
from bs4 import BeautifulSoup

def get_data():
   cur_date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
   with open(f'labirint_{cur_date}.csv', 'w') as file:
       writer = csv.writer(file)

       writer.writerow(
           (
               'Название книги',
               'Автор',
               'Издательство',
               'Цена со скидкой',
               'Цена без скидки',
               'Процент скидки',
               'Наличие на складе'
           )
       )
   headers = {
       "accept": "text / html, * / *;q = 0.01",
       "accept-encoding": "gzip, deflate, br",
       "accept-language": "ru, en;q = 0.9, en - GB;q = 0.8, en - US;q = 0.7",
       'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29'
   }
   url = 'https://www.labirint.ru/genres/2308/?availible=1&paperbook=1&display=table'
   r = requests.get(url=url, headers=headers)

   soup = BeautifulSoup(r.text, 'lxml')
   pages_count = int(soup.find('div', class_="pagination-numbers").find_all("a")[-1].text)
   books_data = []
   for page in range(1, pages_count + 1):
       url = f'https://www.labirint.ru/genres/2308/?availible=1&paperbook=1&display=table&page={page}'

       r = requests.get(url=url, headers=headers)
       soup = BeautifulSoup(r.text, 'lxml')
       books_items = soup.find("tbody", class_="products-table__body").find_all("tr")

       for bi in books_items:
           book_data = bi.find_all("td")
           # print(book_data)
           try:
               book_title = book_data[0].find('a').text.strip()
           except:
               book_title = 'Нет названия'
           try:
               book_author = book_data[1].find('a').text.strip()
           except:
               book_author = 'Нет автора'
           try:
               book_publishing = book_data[2].find('a').text.strip()
           except:
               book_publishing = 'Нет издательства'
           try:
               book_new_price = int(book_data[3].find('div', class_='price').find('span', class_='price-val').find('span').text.strip().replace(" ", ""))
           except:
               book_new_price = 'Нет новой цены'
           try:
               book_old_price = int(book_data[3].find('span', class_='price-gray').text.strip().replace(" ", ""))
           except:
               book_old_price = 'Нет старой цены'
           try:
               book_sale = round(((book_old_price - book_new_price) / book_old_price) * 100)
           except:
               book_sale = 'Нет старой цены'
           try:
               book_status = book_data[-1].text.strip()
           except:
               book_status = 'Нет статуса'
           books_data.append(
               {
                   'book_title': book_title,
                   'book_author': book_author,
                   'book_publishing': book_publishing,
                   'book_new_price': book_new_price,
                   'book_old_price': book_old_price,
                   'book_sale': book_sale,
                   'book_status': book_status,
               }
           )
           with open(f'labirint_{cur_date}.csv', 'a') as file:
               writer = csv.writer(file)

               writer.writerow(
                   (
                       book_title,
                       book_author,
                       book_publishing,
                       book_new_price,
                       book_old_price,
                       book_sale,
                       book_status
                   )
               )
       print(f'Обработана {page}/{pages_count}')
       time.sleep(1)
   with open(f'labirint_{cur_date}.json', 'w') as file:
       json.dump(books_data, file, indent=4, ensure_ascii=False)

def main():
   get_data()



if __name__ ==  '__main__':
   main()
