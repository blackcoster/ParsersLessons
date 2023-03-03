from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
# bs.span vs bs.find('span',{'class':'1'})
nameList = bs.find_all('span',{'class':'green'},limit=3)
# for i in nameList:
#     print(i.get_text())
# ans = bs.body.find_all(['h1','h2','h3'],recursive=)
# print(ans)
names = bs.find_all(string='the prince',limit=3)
print(len(names))
