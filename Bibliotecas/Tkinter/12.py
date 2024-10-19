from tkinter import *

tela = Tk()
#primeiro aprendi sobre o metodo geometry, e depois sobre o metodo state
tela.state("normal") #tela normal
tela.state("zoomed") # tela cheia
tela.state("withdrawn") # fechar tela
tela.state("iconic") #minimizar tela

mainloop()