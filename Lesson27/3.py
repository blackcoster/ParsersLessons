from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')

s = bs.div.find('div').previous_siblings
for i in s:
    print(i)