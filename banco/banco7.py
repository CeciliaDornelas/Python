import sqlite3 as conector

#abertura de conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys=on")
cursor = conexao.cursor()

#definição de comandos 
comando = ''' DELETE FROM pessoa WHERE cpf= 00000000000;'''
cursor.execute(comando)

#efetivação do comando 
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()