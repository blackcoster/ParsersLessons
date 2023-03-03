from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')

s = bs.find('img',{'src':"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
print(s)
