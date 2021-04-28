# abrir
#open("teste.txt")
#print ("aberto com sucesso")

#import os

#arquivo1= open("teste.txt")
#arquivo2= open("C:/Users/cecilia/Desktop/testar/teste2.txt")

#print(os.path.realpath(arquivo1.name))
#print(os.path.abspath(arquivo2.name))

#print(arquivo1)

#arq= open("teste.txt")

#print("nome do arquivo: ",arq.name)
#print("modo do arquivo: ", arq.mode)
#print("arquivo fechado: ",arq.closed)
# fechar aquivo
#arq.close()

#print("arquivo fechado: ",arq.closed)
# ler arquivo
#arquivo = open("notas.txt","r")

#conteudo = arquivo.read()

#print("tipo de conteudo:", type(conteudo))

#print("conteudo retornado pelo read:")
#print(repr(conteudo))

#arquivo.close()

# ler arquivo linha por linha
#arquivo = open("teste.txt")

#conteudo = arquivo.readline()

#prox_conteudo = arquivo.readline()

#print("proximo conteudo retornado:")
#print(repr(prox_conteudo))

#arquivo.close()

#arquivo = open("teste.txt")

#print("todo o conteudo do arquivo:")
#print(repr(conteudo),'\n')

#conteudo_releitura = arquivo.read()
#print("releitura de todo o conteudo do arquivo")
#print(repr(conteudo_releitura),'\n')

#arquivo.close()

#arquivo_reaberto = open("text.txt","r")

#conteudo_reaberto = arquivo_reaberto.read()
#print("todo o conteudo do arquivo reaberto:")
#print(repr(conteudo_reaberto),'\n')

#arquivo_reaberto.seek(0)
#conteudo_seek = arquivo_reaberto.read()
#print("todo conteudo do arquivo seek:")
#print(repr(conteudo_seek))

#arquivo.close()