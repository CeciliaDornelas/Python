import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' CREATE TABLE aula(
    codigo_aula INTEGER NOT NULL,
    turma TEXT NOT NULL,
    nome_disciplina TEXT NOT NULL,
    FOREIGN KEY(turma) REFERENCES alunos(turma),
    FOREIGN KEY(nome_disciplina) REFERENCES disciplina(nome_disciplina),
    PRIMARY KEY(codigo_aula));'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()