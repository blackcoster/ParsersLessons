from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://docs.python.org/3/reference/index.html'
html = urlopen(url)
bs = BeautifulSoup(html,'html.parser')
ssilki = bs.find_all('a')
for ssilka in ssilki:
    ans = ssilka.get('href')
    print(ans)
    # match = re.search(r'https.*', ans)
    # print(match[0] if match else None)



