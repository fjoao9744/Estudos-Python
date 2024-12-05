import sqlite3

conn = sqlite3.connect("data.db") 
cursor = conn.cursor()


''' Juntando tudo '''
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS smogon (
        nome TEXT
    )""")

    conn.commit()

def insert_info(text):
    cursor.execute("""INSERT INTO smogon (nome)
    VALUES (?)
    """, (text,))

    conn.commit()

def table():
    cursor.execute("""
    SELECT * FROM smogon
    """)

    nomes = cursor.fetchall()
    for _ in nomes:
        print(_)

def delete_table():
    cursor.execute("""
    DROP TABLE IF EXISTS smogon
    """) 

    conn.commit()



create_table()
insert_info("teste 2")
table()
delete_table()

# fecha o cursor e a conecção
cursor.close()
conn.close()