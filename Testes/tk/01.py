from tkinter import *

janela = Tk()
janela.geometry('300x300')



senha = Entry(janela, width=30)
senha.grid(row=0, column=0)



texto = Label(janela, text='0')
texto.grid(row=1, column=0)

def subs():
    get = senha.get()
    texto['text'] = get

botao = Button(janela, text='aperte aqui', command=subs)
botao.grid(row=2, column=0)

janela.mainloop()

