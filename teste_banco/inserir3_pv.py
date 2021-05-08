import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' INSERT INTO turmas(codigo_turma,turma,nome,turno)
VALUES('01','gato','Cecilia','noite')'''
cursor.execute(comando)

comando1 = ''' INSERT INTO turmas(codigo_turma,turma,nome,turno)
VALUES('02','cachorro','Antonio','manhã')'''
cursor.execute(comando1)

comando2 = ''' INSERT INTO turmas(codigo_turma,turma,nome,turno)
VALUES('03','cachorro','Paola','noite')'''
cursor.execute(comando2)

comando3 = ''' INSERT INTO turmas(codigo_turma,turma,nome,turno)
VALUES('04','crocodilo','Anastacia','tarde')'''
cursor.execute(comando3)

comando4 = ''' INSERT INTO turmas(codigo_turma,turma,nome,turno)
VALUES('05','papaguaio','Yonara','tarde')'''
cursor.execute(comando4)

conexao.commit()

cursor.close()
conexao.close()