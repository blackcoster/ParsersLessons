import json
from urllib.request import urlopen

def getCountry(ip):
    response = urlopen(f'http://ip-api.com/json/{ip}').read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('city')

print(getCountry('122.55.67.100'))