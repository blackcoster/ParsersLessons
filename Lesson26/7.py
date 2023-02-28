import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page3.html'
html = requests.get(url)

bs = BeautifulSoup(html.text,'html.parser')
table = bs.table
tr = table.find('tr','gift')

print(tr.contents[2].text.strip())
