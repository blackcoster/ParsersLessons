import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup

def links(name,bs):
    a = bs.find_all('a')
    for item in a:
        i =item.get_text()
        print(f'{name}----{i}')

def fat(name,bs):
    a = bs.find_all('b')
    for item in a:
        i =item.get_text()
        print(f'{name}----{i}')
#
html = urlopen('https://en.wikipedia.org/wiki/Witchfinder_General_(film)')
bs = BeautifulSoup(html,'html.parser')
#

threading.Thread(target=links, args=('PPPP', bs)).start()
threading.Thread(target=fat, args=('ooooo', bs)).start()

