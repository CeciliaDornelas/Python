import sqlite3 as conector

try:
    #abertura de conexão e aquisição de cursor 
    conexao = conector.connect("./meu_banco.db")
    cursor=conexao.cursor()

    #execução de um comando

    comando = ''' CREATE TABLE Veiculo(
        placa CHARACTER(7) NOT NULL,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        proprietario INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
        FOREIGN KEY (marca)REFERENCES Marca(id)
    );'''
    
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