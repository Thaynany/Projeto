import sqlite3
# 1- Conectando no BD
conexao=sqlite3.connect('novela.db')
cursor=conexao.cursor()

# 2-Exclusão
id = (1,2)
cursor.execute(
    """
    DELETE FROM novela
    WHERE id in (?,?)
    """,
    id
)
conexao.commit()