from tkinter import *

tela = Tk()

e = Entry(tela) #criando uma entry 
e.pack()

def add():
    e.insert(0, "texto") #insert adiciona um texto a uma posição na caixa de entrada 

botao_add = Button(tela, text="adicionar texto", command=add) 
botao_add.pack()

def remove():
    e.delete(0, END) #delete remove o texto da caixa de entrada(o END esta falando "apague da posição 0 até o final")

botao_del = Button(tela, text="remove texto", command=remove)
botao_del.pack()

mainloop()