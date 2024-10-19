from tkinter import *

tela = Tk()

e = Entry(tela) 
e.pack()

e.insert(0, "texto padrão ") #adicionar texto 

def esconder():
    e.delete(0, "end") #deletar o texto


botao = Button(tela, text="apagar entry", command=esconder).pack()



mainloop()