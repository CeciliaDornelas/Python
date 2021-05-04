import sqlite3 as conector
from classe_banco import pessoa

#abertura de coneção e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#criação de um objeto do tipo pessoa
pessoa = pessoa(00000000000,'Antonio','1975-05-16',False)

#definição de um comando com query paranater
comando = ''' INSERT INTO pessoa(cpf,nome,nascimento,oculos)VALUES(?, ?, ?, ?)'''
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()
