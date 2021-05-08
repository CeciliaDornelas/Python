import sqlite3 as conector

conexao = conector.connect("./banco_escola.db")
cursor = conexao.cursor()

#comando = ''' INSERT INTO alunos(matricula,nome,nascimento,tel) VALUES(202002546263,'Cecilia','2002-03-16',40028922)'''
#cursor.execute(comando)

comando = ''' INSERT INTO profs(matricula,nome,nascimento,tel) VALUES(202003562142,'Antonio','1995-05-16',32212917)'''
cursor.execute(comando)

comando = ''' INSERT INTO curso(cod,nome,tipo,turno,semestres) VALUES(170,'ADS','presencial','noite',5)'''
cursor.execute(comando)

conexao.commit()


cursor.close()
conexao.close()