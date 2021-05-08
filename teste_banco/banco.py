import sqlite3 as conector

try: 
    conexao = conector.connect("./banco_escola.db")
    cursor = conexao.cursor()

    comando = ''' CREATE TABLE alunos(
        matricula INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        tel INTEGER NOT NULL,
        PRIMARY KEY(matricula)
        );'''
    cursor.execute(comando)

    comando = ''' CREATE TABLE profs(
        matricula INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        tel INTEGER NOT NULL,
        PRIMARY KEY(matricula)
        );'''
    cursor.execute(comando)

    comando = ''' CREATE TABLE curso(
        cod INTEGER NOT NULL,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        turno TEXT NOT NULL,
        semestres INTERGER NOT NULL,
        PRIMARY KEY(cod)
        );'''
    cursor.execute(comando)
    
    conexao.commit()
except conector.DatabaseError as erro:
    print("erro de banco de dados",erro)
finally:
    if conexao:
        cursor.close()
        conexao.close()