import sqlite3

# 1- Conectando no BD
conexao=sqlite3.connect('novela.db')

cursor=conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO novela(nome, ano_lancamento, audiencia_media)
        VALUES ('Pantanal', 2022, 9.0)
    """
)

conexao.commit()
conexao.close()