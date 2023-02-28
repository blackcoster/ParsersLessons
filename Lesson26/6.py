from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.title
    except AttributeError:
        return None
    return title


t = getTitle('https://www.pythonscraping.com/pages/page1.html')
if t == None:
    print('Заголовок не был найден')
else:
    print(t.text)
