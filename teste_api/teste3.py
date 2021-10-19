import requests
import json

token = 'Bearer '
url = ''
id_cliente = ''

headers = {
    'access_token': token,
    'client_id': id_cliente,
    'Accept-Encoding': "br, deflate, gzip",
    'Accept': "*/*", 
    'User-Agent': "python-requests/1.2.0",
    'Connection': "keep-alive"
}

parametros = {

}

busca = requests.get(url=url, headers=headers, params=parametros)
busca = busca.json()
print(busca)

    
