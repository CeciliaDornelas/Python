import os

# dados para entrar
nome = input("digite o nome do aluno: ")
mat = input("digite o numero da matricula:")
n1 = input("digite a primeira nota: ")
n2 = input("digite a segunda nota: ")
n3 = input("digite a terceira nota: ")


#adicionar ao arquivo notas.txt
arqv = open("C:/Users/cecilia/Desktop/prog/Python/alunos/notas.txt","a")
arqv.write(f"nome: {nome} matricula: {mat} \n nota 1: {n1}  nota 2: {n2} nota 3: {n3} \n")

arqv.close()
#arqv.closed

#ler conteudo
with open("C:/Users/cecilia/Desktop/prog/Python/alunos/notas.txt","r") as arquivo:

    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))

arqv.close()
