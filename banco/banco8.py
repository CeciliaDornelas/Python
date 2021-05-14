import sqlite3 as conector

#abertura de conexao e aquisição de cursor 
conexao= conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#definição dos registros
comando = '''SELECT nome,oculos FROM pessoa;'''
cursor.execute(comando)

#recuperação dos dados
registros = cursor.fetchall()
print("tipo retornado pelo fetchall():",type(registros))

for registro in registros:
    print("tipo",type(registro), "- conteudo", registro)

#fechamento das conexões
cursor.close()
conexao.close()