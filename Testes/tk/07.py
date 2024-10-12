from tkinter import *

tela = Tk()

l1 = Label(tela, text="linha 1", padx=50)
l1.grid(row=0, column=0)

print(l1.configure().keys()) # mostra todas as funções do objeto

mainloop()


