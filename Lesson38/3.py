import requests
#куки аутентификация
params = {'username':'qwerty',
          'password':'password'}

r = requests.post('https://pythonscraping.com/pages/cookies/welcome.php',data = params)
print('cookie is set to:')
print(r.cookies.get_dict())
print('going to profile page')
r = requests.get('https://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
print(r.text)

