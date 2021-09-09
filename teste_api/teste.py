import requests
import json

cotacoes = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

cotacao_dolar = cotacoes['USDBRL'] ["bid"]
cotacao_euro = cotacoes['EURBRL'] ["bid"]
cotacao_bitcoin = cotacoes['BTCBRL'] ["bid"]

#print(cotacoes)
print("A cotaçao do Euro eh " + cotacao_euro)
print("A cotação do Dolar eh " + cotacao_dolar)
print("A cotaçao do Bitcoin eh " + cotacao_bitcoin)