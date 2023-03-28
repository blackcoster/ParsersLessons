from urllib.request import  urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com')
bs = BeautifulSoup(html,'html.parser')
imageLocation = bs.find('img',class_ = 'pagelayer-img pagelayer-animation-{{anim_hover}}')['src']
urlretrieve(imageLocation,'logo.jpg')