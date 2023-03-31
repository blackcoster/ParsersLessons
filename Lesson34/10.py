import requests
from bs4 import BeautifulSoup
import lxml

textPage = requests.get('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(textPage.text,'lxml')
content =bs.find('div',{'id':'mw-content-text'}).get_text()
content = bytes(content,'UTF-8')
content = content.decode('UTF-8')
print(content)