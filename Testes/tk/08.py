from tkinter import *

tela = Tk()

l1 = Label(tela, text="linha 1", padx=50, fg="blue")
l1.grid(row=0, column=0)

texto = l1['text']

print(texto)

mainloop()


