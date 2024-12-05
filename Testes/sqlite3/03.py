import sqlite3

conn = sqlite3.connect("data.db") 

cursor = conn.cursor()

# insere na tabela smogon na coluna nome os valores (?)
cursor.execute("""INSERT INTO smogon (nome)
VALUES (?)
""", ("smogon",)) # esses valores (?) ficam aqui

conn.commit()