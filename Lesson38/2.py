import requests

files = {'uploadFile': open('file1.txt','rb')}
r = requests.post('https://pythonscraping.com/pages/files/processing2.php',files=files)
print(r.text)

