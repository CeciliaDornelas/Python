import sqlite3 as conector

#abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#execução de um comando: SELECT...CREATE...
comando = '''INSERT INTO pessoa(cpf,nome,nascimento,oculos)
    VALUES(40028922127,'cecilia','2002-03-16',0);'''

cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()

