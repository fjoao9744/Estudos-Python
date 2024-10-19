from tkinter import *

tela = Tk()

l = Label(tela, text="esse texto sera escondido") #esconder texto
l.pack()

def esconder():
    l.pack_forget()

botao = Button(tela, text="esconder label", command=esconder).pack()



mainloop()