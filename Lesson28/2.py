import requests

url = 'https://www.kinopoisk.ru/media/article/4007433/'
r = requests.get(url)
print(r.status_code)
print(r.raise_for_status())
if r.raise_for_status()==None:
    pass
# 100-199 информационные
# 200-299 успешные
# 300-399 перенаправлния
# 400-499 клиентские ошибки
# 500-599 - сервер ошибки