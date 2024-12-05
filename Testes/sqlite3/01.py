import sqlite3

conn = sqlite3.connect("data.db") # conecta no banco de dados

cursor = conn.cursor() # cria um cursor para conseguir fazer alterações no banco de dados

# cria uma tabela
cursor.execute("CREATE TABLE smogon (nome TEXT)")

# atualiza informações que o cursor fez no banco de dados
conn.commit()

