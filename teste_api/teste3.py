import requests
import json

token = 'Bearer '
url = ''

headers = {
    'Authorization': token
}

busca = requests.get(url=url, headers=headers )
busca = busca.json()

print(busca)
    
