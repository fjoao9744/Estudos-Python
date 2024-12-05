# Importações
import sqlite3 
from tkinter import *

# estabelecendo conecção com o banco de dados
connection = sqlite3.connect("Banco de dados.db")
cursor = connection.cursor()

# configurações padrão da janela
screen = Tk()
screen.geometry("700x440+540+200")
screen.title("Manipulador de banco de dados")

# função que vai adicionar um novo item no DB 
def add_data(event=None):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS database (
    texto TEXT
    )""")
    cursor.execute("""
    INSERT INTO database (texto)
    VALUES (?)
    """, (add_entry.get(),))
    connection.commit()
    
    update()

# função que vai apagar todos os itens do DB com aquele texto
def delete_data(event=None):
    cursor.execute("""
    DELETE FROM database WHERE texto = ?
    """, (add_entry.get(),))
    connection.commit()

    update()

titulo = Label(screen, text="teste com banco de dados",font=("Arial",20)).pack()

data_list = Listbox(screen, height=20, width=80)
data_list.pack()

add_entry = Entry(screen)
add_entry.pack()

add_button = Button(screen, text="Adicionar texto", command=add_data)
add_button.pack()

delete_button = Button(screen, text="deletar texto", command=delete_data)
delete_button.pack()

# função que vai atualizar o list_box
def update(event=None):
    data_list.delete(0, END)
    cursor.execute("""
    SELECT * FROM database
    """)
    datas = cursor.fetchall()
    for dt in datas:
        data_list.insert(END, dt)
    data_list.see(END)

update()

mainloop()