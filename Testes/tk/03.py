#dado

from tkinter import *
from random import randrange


app = Tk()

texto = Label(app, text="NaN")
texto.grid(row=0, column=0)

def d6():
    numero = randrange(1, 7)

    texto['text'] = str(numero)

def d20():
    numero = randrange(1, 21)

    texto['text'] = str(numero)
def d100():
    numero = randrange(1, 101)

    texto['text'] = str(numero)

Button(app, text="d6", command=d6).grid(row=1, column=0)
Button(app, text="d20", command=d20).grid(row=1, column=1)
Button(app, text="d100", command=d100).grid(row=1, column=2)






mainloop()