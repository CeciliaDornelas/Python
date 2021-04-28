import os, sys, stat
#(i)
try:
    aqv=open("")
    aqv.close("C:/Users/cecilia/Desktop/prog/Python/alunos/notas.txt")
except OSError as erro:
    print(erro)
    print("doc não foi aberto")

#(ii)
arquivo = open('testando.txt', 'w')
arquivo.close()

#mudando comando so para leitura
os.chmod("testando.txt", stat.S_IREAD)

try:
  aqv=open("testando.txt", "w")
  print("Arquivo Aberto")
  aqv.write("oi")
  aqv.close()
except PermissionError as erro:
    print(erro)
    print("Você não tem essa permissão")

#(iii)
try:
  open("teste.pdf", "r")
  print("Arquivo Aberto")
except FileNotFoundError as erro:
    print(erro)
    print("Arquivo não existe")
 