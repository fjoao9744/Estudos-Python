from tkinter import *

tela = Tk()

def on_click(event=None): #passamos o event none para evitar erros que podem acontecer ja que o tkinter gosta que funções retornem coisas
    botao.config(text="espere", state=DISABLED)

    tela.after(2000, reset) #o after faz com que tenha uma pausa e rode uma função no final da pausa

def reset(event=None):
    botao.config(text="me aperte", fg="green", state=NORMAL) #reconfigurando o botao

botao = Button(tela, text="me aperte", fg="green", command=on_click)
botao.pack()

mainloop()