import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

downloadDirectory = 'downloaded/'
baseUrl = 'pythonscraping.com/'

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace('https://','')
    path = path.replace(baseUrl,'')
    path = path.replace('wp-content/','')
    path = path.replace('uploads/2021/08/', '')
    path = downloadDirectory+ path

    directory = os.path.dirname(path)
    print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen('https://pythonscraping.com/')
bs = BeautifulSoup(html,'lxml')
downloadList = bs.findAll(src=True)
# print(downloadList)
for download in downloadList:
    fileUrl = download['src']
    # print(fileUrl)
    if 'uploads' in fileUrl:
        # print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))







