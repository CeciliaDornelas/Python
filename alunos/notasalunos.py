import os

# dados para entrar
nome = input("digite o nome do aluno: ")
n1 = input("digite a primeira nota: ")
n2 = input("digite a segunda nota: ")
n3 = input("digite a terceira nota: ")


#adicionar ao arquivo notas.txt
arqv = open("C:/Users/cecilia/Desktop/prog/Python/alunos/notas.txt","a")
arqv.write(" nome:")
arqv.write(nome)
arqv.write("\n primeira nota:")
arqv.write(n1)
arqv.write(" segunda nota:")
arqv.write(n2)
arqv.write(" terceira nota:")
arqv.write(n3)
arqv.write("\n")

arqv.close()

#ler conteudo
arqv = open("C:/Users/cecilia/Desktop/prog/Python/alunos/notas.txt","r")
conteudo = arqv.read()

print("conteudo retornado pelo read:")
print(repr(conteudo))

arqv.close()
