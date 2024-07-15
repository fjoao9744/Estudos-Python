from tkinter import *
from random import randint
janela = Tk()

def contador():
    numero['text'] = randint(0, 10)
        


    

botao = Button(janela, text='clique', command=contador)
botao.grid(column=0, row=0)
numero = Label(janela, text='')
numero.grid(column=0, row=1)
texto = Label(janela, text='smogon')
texto.grid(column=0, row=2)

janela.mainloop()