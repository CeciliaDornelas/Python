import sqlite3 as conector
from classe_banco import pessoa
#abertura de conexao e aquisição de cursor 
conexao= conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#definição dos registros
comando = '''SELECT * FROM pessoa WHERE oculos =:usa_oculos;'''
cursor.execute(comando, {"usa_oculos":True})

#recuperação dos dados
registros = cursor.fetchall()

for registro in registros:
    pessoa1 = pessoa(*registro)
    print("cpf:",type(pessoa1.cpf), pessoa1.cpf)
    print("nome:",type(pessoa1.nome), pessoa1.nome)
    print("nascimento:",type(pessoa1.data_nascimento), pessoa1.data_nascimento)
    print("oculos:",type(pessoa1.usa_oculos), pessoa1.usa_oculos)

#fechamento das conexões
cursor.close()
conexao.close()