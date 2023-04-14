import requests

params = {'firstname':'Соня',
          'lastname':'Тренина'}

r = requests.post('https://pythonscraping.com/pages/files/processing.php',data = params)
print(r.text)
