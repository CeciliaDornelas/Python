import sqlite3 as conector

#abertura de conexão e aquisição
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys=on")
cursor = conexao.cursor()

#definição de comandos
comando1 = '''UPDATE pessoa SET oculos = 1;'''
cursor.execute(comando1)

comando2 = '''UPDATE pessoa SET oculos= ? WHERE cpf= 00000000000;'''
cursor.execute(comando2, (False,))

comando3 = '''UPDATE pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
cursor.execute(comando3, {"usa_oculos": True, "cpf": 40028922127})

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()