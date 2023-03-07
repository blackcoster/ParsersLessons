from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs  = BeautifulSoup(html,'html.parser')
r = re.compile('../img/gifts/img.*.jpg')
images = bs.find_all('img',{'src':r})
for image in images:
    print(image['src'])


