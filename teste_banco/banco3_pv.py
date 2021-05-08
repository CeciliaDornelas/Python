import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' CREATE TABLE turmas(
    codigo_turma INTEGER NOT NULL,
    turma TEXT NOT NULL,
    nome TEXT NOT NULL,
    turno TEXT NOT NULL,
    FOREIGN KEY(turma) REFERENCES alunos(turma),
    FOREIGN KEY(nome) REFERENCES alunos(nome_aluno),
    PRIMARY KEY(codigo_turma));'''

cursor.execute(comando)


conexao.commit()

cursor.close()
conexao.close()