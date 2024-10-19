from tkinter import *

tela = Tk()

#criar funções que alteram a tela
def normal():
    tela.state("normal")

def zoomed():
    tela.state("zoomed")

def withdrawn():
    tela.state("withdrawn")

def iconic():
    tela.state("iconic")

#criar botões para alterar a tela
botao_normal = Button(tela, text="normal", command=normal).pack()
botao_iconic = Button(tela, text="zoomed", command=zoomed).pack()
botao_withdrawm = Button(tela, text="withdrawn", command=withdrawn).pack()
botao_zoomed = Button(tela, text="iconic", command=iconic).pack()

mainloop()