
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# ../img/gifts/img2.jpg
r=re.compile('../img/gifts/img.*.jpg')
images = bs.find_all('img',{'src':r})
for image in images:
    print(image['src'])

# # 1) хотя бы 1 буква а      aa*
# # 2) ровно 5 букв б         ббббб
# # 3) четное число букв в    (вв)*
# # 4) в конце буква г или д  (д|е)
# r=re.compile('аа*ббббб(вв)*(д|е)')



