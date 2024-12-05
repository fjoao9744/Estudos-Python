import sqlite3

conn = sqlite3.connect("data.db") 

cursor = conn.cursor()

# só cria a tabela se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS smogon (
    nome TEXT
)""")

conn.commit()

# seleciona tudo da tabela smogon
cursor.execute("""
SELECT * FROM smogon
""")

# pega o resultado da seleção
nomes = cursor.fetchall()

for _ in nomes:
    print(_)

