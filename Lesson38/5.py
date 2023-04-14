import requests
from requests.auth import AuthBase,HTTPBasicAuth
#HTTP - аутентификация
auth = HTTPBasicAuth('polina','1234567890')
r = requests.post(url='https://pythonscraping.com/pages/auth/login.php',auth=auth)
print(r.text)