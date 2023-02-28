from urllib.error import HTTPError, URLError
from  bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    url = 'https://www.pythonscraping.com/pages/page1.html'
    html = urlopen(url)
except HTTPError:
    print('на сайте нет такой страницы')
except URLError:
    print('нет такого сайта')
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    try:
        badContent = bs.b
    except AttributeError :
        print('тег не найден1')
    else:
        if badContent == None:
            print('тег не найден')
        else:
            print(badContent)
