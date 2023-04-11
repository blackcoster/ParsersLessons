Реализовать парсер скачивающий картинки по ссылке
'https://www.wallpaperbetter.com/ru/search?q=%D0%BF%D1%80%D0%B8%D1%80%D0%BE%D0%B4%D0%B0


images = bs.find_all('img',class_ = 'lazy')

for i,im in enumerate(images):
    url = im.get('data-src')
    code = requests.get(url)
    with open(f'img{i}.jpg','wb') as file:
        file.write(code.content)
        print(f'complete img{i}')