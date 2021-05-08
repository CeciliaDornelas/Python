import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' CREATE TABLE alunos(
    matricula INTEGER NOT NULL,
    cpf INTEGER NOT NULL,
    nascimento DATE NOT NULL,
    turma TEXT NOT NULL,
    nome_aluno TEXT NOT NULL,
    endereco TEXT NOT NULL,
    PRIMARY KEY(matricula));'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()