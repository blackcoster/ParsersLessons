import csv
import json

import requests
from bs4 import BeautifulSoup

books = []
def parse(link):
    global books

    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='vib')
    for i in items:
        itemName = i.find('a', class_='Bib').text.strip()
        itemAuthor = i.find('div', class_='wib').text.strip()
        itemPrice = ...

        books.append([itemName,itemAuthor,...])

parse('https://www.bookvoed.ru/')

with open('list.csv','w',encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for row in books:
        writer.writerow(row)


with open('k.xml','w',encoding='utf-8') as file:
    file.write('<items>\n')
    for u in books:

        file.write('    <item>\n')
        file.write(f'        <название>{u[0]}</название>\n')
        file.write(f'        <автор>{u[1]}</автор>\n')
        file.write(f'        <price>{...}</price>\n')
        file.write('    </item>\n')
    file.write('</items>\n')