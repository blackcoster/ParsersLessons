from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

from bs4 import BeautifulSoup

wordFile = urlopen('https://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)

xml_content = document.read('word/document.xml')
bs = BeautifulSoup(xml_content.decode('utf-8'),'xml')
text = bs.findAll('w:t')
print(bs)
for t in text:
    style = t.parent.parent.find('w:pStyle')
    if style is not None and style['w:val']=='Title':
        print(f'Title is: {t.text}')
    else:
        print(t.text.strip())
    # print(t.text.strip())

# print(xml_content.decode('utf-8'))  ПОСМОТРЕТЬ КОД ФАЙЛА
