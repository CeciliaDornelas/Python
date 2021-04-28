import sqlite3 as conector

try:
    #abertura de conexão e aquisição de cursor 
    conexao = conector.connect("./meu_banco.db")
    cursor=conexao.cursor()

    comando = '''ALTER TABLE  Veiculo
    ADD motor REAL;'''
    
    cursor.execute(comando)
    
    # efetivação do comando
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de banco de dados",erro)

finally:
    #fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()