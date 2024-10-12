from tkinter import *

tela = Tk()

l1 = Label(tela, text="temos um texto 1")
l1.pack() #a diferença entre o pack e o grid, é que o grid funciona em uma grade enumerada enquanto o pack relativo aos conteiner(inclusive a tela)
#lado padrão = topo

#agora vamos criar outras labels para exemplificar
l2 = Label(tela, text="temos um text 2")
l2.pack()

l3 = Label(tela, text="temos um text 3")
l3.pack()

l4 = Label(tela, text="temos um text 4")
l4.pack()

l5 = Label(tela, text="temos um text 5")
l5.pack()

l6 = Label(tela, text="temos um texto a direita") # vamos criar um texto a direita
l6.pack(side="right")

l7 = Label(tela, text="temos outro texto") # esse texto vai expandir seu padding
l7.pack(expand=1)

l8 = Label(tela, text="temos outro texto") # e esse não
l8.pack(expand=0)




mainloop()