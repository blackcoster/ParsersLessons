import csv
import json

import requests
from bs4 import BeautifulSoup

goods = []
headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/95.0.4638.69 Safari/537.36"
    }
def parse(link):
    global goods

    url = link
    html = requests.get(url,headers=headers)
    bs = BeautifulSoup(html.text, 'html.parser')
    items = bs.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip()
        ssilka = i.find('h4').find('a').get('href')
        itemPrice = i.find('h5').text


        print(ssilka)
        html = requests.get('https://scrapingclub.com'+ssilka, headers=headers)
        bs = BeautifulSoup(html.text, 'html.parser')
        content = bs.find('p',class_='card-text').text.strip()

        goods.append([itemName,..., content])


for i in range(1,8):
    parse(f'https://scrapingclub.com/exercise/list_basic/?page={i}')


# csvFile = open('list.csv','w',encoding = 'utf-8')
# writer = csv.writer(csvFile)
# for row in goods_csv:
#     writer.writerow(row)
# csvFile.close()



with open('k.xml','w',encoding='utf-8') as file:
    file.write('<items>\n')
    for good in goods:

        file.write('    <item>\n')
        file.write(f'        <name>{good[0]}</name>\n')
        file.write(f'        <price>{...}</price>\n')
        file.write(f'        <content>{good[2]}</price>\n')
        file.write('    </item>\n')
    file.write('</items>\n')