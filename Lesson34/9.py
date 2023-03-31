from urllib.request import urlopen
page = 'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt'
textpage = urlopen(page)

print(str(textpage.read(),'utf-8'))

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html,'html.parser')
content = bs.find('div',{'id':'mw-content-text'}).get_text()
content = bytes(content,'UTF-8')
content = content.decode('UTF-8')
print(content)


