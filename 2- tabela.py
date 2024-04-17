import sqlite3

# 1- Conectando no BD
conexao=sqlite3.connect('novela.db')

cursor=conexao.cursor()

# 2-Criação da Tabela de novela
cursor.execute(
    """
        CREATE TABLE NOVELA(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
          nome TEXT NOT NULL,
          ano_lancamento INTEGER NOT NULL,
          audiencia_media REAL 
        );
    """
)
# 3- Fecha conexão
conexao.close()
print("Tabela foi criada")