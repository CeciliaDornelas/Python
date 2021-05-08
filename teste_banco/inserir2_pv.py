import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' INSERT INTO disciplina(codigo_disciplina,nome_diciplina,carga_horaria,conteudo)
VALUES(01,'JAVA',50,'aula de linguagem java')'''
cursor.execute(comando)

comando1 = ''' INSERT INTO disciplina(codigo_disciplina,nome_diciplina,carga_horaria,conteudo)
VALUES(02,'JAVASCRIPT',30,'aula de linguagem javascript')'''
cursor.execute(comando1)

comando2 = ''' INSERT INTO disciplina(codigo_disciplina,nome_diciplina,carga_horaria,conteudo)
VALUES(03,'PYTHON',80,'aula de linguagem python')'''
cursor.execute(comando2)

comando3 = ''' INSERT INTO disciplina(codigo_disciplina,nome_diciplina,carga_horaria,conteudo)
VALUES(04,'PHP',30,'aula de linguagem php')'''
cursor.execute(comando3)

comando4 = ''' INSERT INTO disciplina(codigo_disciplina,nome_diciplina,carga_horaria,conteudo)
VALUES(05,'C',90,'aula de linguagem e estruturas em C')'''
cursor.execute(comando4)

conexao.commit()

cursor.close()
conexao.close()