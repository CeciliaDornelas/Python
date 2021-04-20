import os

print("abrindo aquivo")

try: 
    open ("dados.txt")
    print("aquivo aberto!")

except FileNotFoundError as erro:
    print("aquivo inexistente")
    print("descrição:",erro)

print("temino do programa")