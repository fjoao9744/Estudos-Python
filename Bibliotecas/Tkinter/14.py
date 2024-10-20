from tkinter import *

tela = Tk()
tela.geometry("300x300")

'''
#pack_forget
def esconder_pack():
    lpack.pack_forget() # o pack_forget esconde as labels, mas lembre-se, não apaga, só esconde

lpack = Label(tela, text="esse texto sera escondido.") #criando uma label para ser escondida
lpack.pack() 

bpack = Button(tela, text="esconder pack", command=esconder_pack).pack()
'''

#grid_forget
def esconder_grid():
    lgrid.grid_forget()

lgrid = Label(tela, text="esse texto sera escondido.")
lgrid.grid() 

bgrid = Button(tela, text="esconder grid", command=esconder_grid).grid()

#place_forget
def esconder_place():
    lplace.place_forget()

lplace = Label(tela, text="esse texto sera escondido.")
lplace.place(x=0, y=100) 

bplace = Button(tela, text="esconder place", command=esconder_place).place(x=0, y=120)


mainloop()