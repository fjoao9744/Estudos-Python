from tkinter import *

calc = 0

janela = Tk()
calc = []
texto = Label(janela, text=calc)
texto.grid(column=0, row=0)


def numero_um():
    global calc
    calc.append(1)
    texto['text'] = calc
def numero_dois():
    global calc
    calc.append(2)
    texto['text'] = calc

def soma():
    global calc
    calc[0] += calc[1]
    texto['text'] = calc


um = Button(janela, text='1', command=numero_um)
um.grid(column=0, row=1)

dois = Button(janela, text='2', command=numero_dois)
dois.grid(column=1, row=1)

mais = Button(janela, text='+', command=numero_dois)
mais.grid(column=2, row=1)

janela.mainloop()