import sqlite3 as conector

conexao = conector.connect("./banco_sistema.db")
cursor = conexao.cursor()

comando = ''' CREATE TABLE disciplina(
    codigo_disciplina INTEGER NOT NULL,
    nome_diciplina TEXT NOT NULL,
    carga_horaria INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    PRIMARY KEY(codigo_disciplina));'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()