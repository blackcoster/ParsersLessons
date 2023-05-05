import json
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getLinks(articleUrl):
    html = urlopen(f'https://en.m.wikipedia.org{articleUrl}')
    bs = BeautifulSoup(html,'html.parser')

    return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIP(pageUrl):
    pageUrl = pageUrl.replace('/wiki/','')
    historyURL = f'https://en.wikipedia.org/w/index.php?title={pageUrl}&action=history'

    print(f'смотрим эту статью - {pageUrl}')
    html = urlopen(historyURL)
    bs = BeautifulSoup(html,'html.parser')

    ipAddress = bs.find_all('a',{'class':'mw-anonuserlink'})
    adressList = set()
    for ip in ipAddress:
        adressList.add(ip.get_text())

    return adressList

def getCountry(ip):
    try:
        response = urlopen(f'http://ip-api.com/json/{ip}').read().decode('utf-8')
    except Exception:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country')

links = getLinks('/wiki/Richard_Feynman')

while len(links)>0:
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIP(link.attrs['href'])
        for ip in historyIPs:
            country = getCountry(ip)
            if country is not None:
                print(f'IP-адрес: {ip}, страна - {country}')

newLink = links[random.randint(0,len(links)-1)].attrs['href']
getLinks(newLink)



