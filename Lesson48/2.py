import json
from time import sleep

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import lxml

def get_data(parsed_sport,pages_amount):
    news_info = []
    for page_number in tqdm(range(1, pages_amount + 1)):
        url = f"https://www.championat.com/news{parsed_sport}{page_number}.html"

        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.text, "lxml")
        all_news = soup.find_all("div", class_="news-item")

        for new in all_news:
            new_time = new.find("div", class_="news-item__time")
            new_content = new.find("div", class_="news-item__content")

            title = new_content.find_all("a")[0].text
            href = "https://www.championat.com" + new_content.find_all("a")[0].get("href")
            tag = new.find("a", class_="news-item__tag").text
            time = new_time.text

            news_info.append({
                "Заголовок": title,
                "Ссылка": href,
                "Тег": tag,
                "Дата публикации": time
            })
        sleep(3)
    with open('news.json','w',encoding='utf-8') as  file:
        json.dump(news_info,file,indent=4,ensure_ascii=False)
    print('смотрите файл')

def person_answer():
    kinds_of_sport = {
        '1. Все новости':'/',
        '2. Футбол':'/football/',
        '3. Хоккей' :'/hockey/',
        '4. Бокс':'/boxing/',
        '5. Теннис':'/tennis/',
        '6. Фигурное катание':'figureskating/'

    }
    count = 1

    for sport in kinds_of_sport.keys():
        print(sport)
        count+=1

    while True:
        input_sport = int(input('Выберете число для вида спорта '))
        dict_key = list(kinds_of_sport.keys())[input_sport-1]
        parsed_sport = kinds_of_sport[dict_key]
        break

    while True:
        pages_amount = int(input('сколько страниц выводить? '))
        break

    return parsed_sport,pages_amount
headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/95.0.4638.69 Safari/537.36"
    }
s,a = person_answer()
get_data(s,a)