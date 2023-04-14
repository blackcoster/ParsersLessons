import requests
#примеры разных файлов
fp = open('file1.txt','rb')
url = 'https://httpbin.org/post'
files = {'file':fp}
files = {'file':(fp,'hello')}

r= requests.post(url,files = files)

