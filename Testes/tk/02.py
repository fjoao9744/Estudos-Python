from tkinter import *


cores = ['azul', 'verde']

janela = Tk()
janela.geometry('300x300')

botao = Button(janela, text='azul')
botao.grid(row=10, column=10)

janela.mainloop()

