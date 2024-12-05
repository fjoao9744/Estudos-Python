import sqlite3

conn = sqlite3.connect("data.db") 
cursor = conn.cursor()

# DROP TABLE apaga uma tabela, porem nesse exemplo ele só apaga se existir uma
cursor.execute("""
DROP TABLE IF EXISTS smogon
""") 

conn.commit()