import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' INSERT INTO aula(codigo_aula,turma,nome_disciplina)
VALUES('01','gato','JAVA')'''
cursor.execute(comando)

comando1 = ''' INSERT INTO aula(codigo_aula,turma,nome_disciplina)
VALUES('02','cachorro','JAVASCRIPT')'''
cursor.execute(comando1)

comando2 = ''' INSERT INTO aula(codigo_aula,turma,nome_disciplina)
VALUES('03','cachorro','PYTHON') '''
cursor.execute(comando2)

comando3 = ''' INSERT INTO aula(codigo_aula,turma,nome_disciplina)
VALUES('04','crocodilo','PHP')'''
cursor.execute(comando3)

comando4 = ''' INSERT INTO aula(codigo_aula,turma,nome_disciplina)
VALUES('05','papaguaio','C')'''
cursor.execute(comando4)

conexao.commit()

cursor.close()
conexao.close()