from tkinter import *

tela = Tk()

def smogon():
    texto['text'] += 'smogon'
    if texto['text'] == 'smogonsmogonsmogon':
        texto['text'] = 'smogon'


texto = Label(tela, text='smogon')
texto.grid(row=0, column=0)

botao = Button(tela, text='aperte aqui', command=smogon)
botao.grid(row=1, column=0)



tela.mainloop()

