import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' INSERT INTO alunos(matricula,cpf,nascimento,turma,nome_aluno,endereco)
VALUES(202002546263,40028922,'2002-03-16','gato','Cecilia','joao pessoa')'''
cursor.execute(comando)

comando1 = ''' INSERT INTO alunos(matricula,cpf,nascimento,turma,nome_aluno,endereco) 
VALUES(20200286524,40028933,'1995-05-16','cachorro','Antonio','joao pessoa')'''
cursor.execute(comando1)

comando2 = ''' INSERT INTO alunos(matricula,cpf,nascimento,turma,nome_aluno,endereco) 
VALUES(20200254672,32218922,'2002-03-01','cachorro','Paola','areia')'''
cursor.execute(comando2)

comando3 = ''' INSERT INTO alunos(matricula,cpf,nascimento,turma,nome_aluno,endereco) 
VALUES(202152546263,40028922,'1955-09-26','crocodilo','Anastacia','rio de janeiro')'''
cursor.execute(comando3)

comando4 = ''' INSERT INTO alunos(matricula,cpf,nascimento,turma,nome_aluno,endereco) 
VALUES(202002559426,40055922,'2001-12-23','papagaio','Yonara','joao pessoa')'''
cursor.execute(comando4)

conexao.commit()


cursor.close()
conexao.close()