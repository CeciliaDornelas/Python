import requests
import json
import os

cep = input("digite seu cep: ")

if len(cep) != 8:
    print("quantidade de digitos invalida!")
    exit()
try:
    busca = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(cep))
    busca = busca.json()

    nome = busca['address']
    uf = busca['state']
    distrito = busca['district']
    cidade = busca['city']
    ddd = busca['ddd']

#print(busca)
 
    print("Resultados:")
    print()
    print("CEP: " + cep + " DDD: " + ddd)
    print(nome + "-" + distrito)
    print(cidade + " "+ uf)
    print()
except:
    print('CEP invalido!')