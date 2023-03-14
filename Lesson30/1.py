import requests
from bs4 import BeautifulSoup
import lxml

class Content:
    def __init__(self,url,title,body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    html = requests.get(url)
    return BeautifulSoup(html.text,'lxml')

def parseBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find('div', {'class', 'post-body'})

    body = '\n'.join([line.text for line in lines])
    return Content(url,title,body)

def parseBootcamp(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find('div', {'class', 'im in io ip iq'})
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
contend = parseBrookings(url)
print(f'Заголовок {contend.title}')
print(f'ссылка {contend.url}')
print(f'содержимое  {contend.body}')

url='https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5'
contend = parseBootcamp(url)
print(f'Заголовок {contend.title}')
print(f'ссылка {contend.url}')
print(f'содержимое  {contend.body}')
#
