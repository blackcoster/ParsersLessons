from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')

deti = bs.find('table').descendants
for i in deti:
    print(i)