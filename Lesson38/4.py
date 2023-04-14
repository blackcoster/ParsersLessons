import requests
#куки аутентификация с памятью
session = requests.Session()
params = {'username':'tykva',
          'password':'password'}
s = session.post('https://pythonscraping.com/pages/cookies/welcome.php',data = params)
print('cookie is set to:')
print(s.cookies.get_dict())
print('going to profile page')
s = session.get('https://pythonscraping.com/pages/cookies/profile.php')
print(s.text)
