from tkinter import *

tela = Tk()
tela.geometry('500x500')


entrada1 = Entry(tela) 
entrada1.pack()

entrada2 = Entry(tela, bd=5).pack() #alterando o tamaho da borda
entrada3 = Entry(tela, bg="blue").pack() #alterando o fundo
entrada4 = Entry(tela, fg="red").pack() #alterando a cor do texto
entrada5 = Entry(tela, justify=CENTER).pack() #deixando o texto no centro
entrada6 = Entry(tela, show="*").pack() # senhas

#relief
entrada7 = Entry(tela, relief=FLAT).pack()
entrada8 = Entry(tela, relief=SUNKEN).pack()
entrada9 = Entry(tela, relief=RAISED).pack()
entrada10 = Entry(tela, relief=GROOVE).pack()





print(entrada1.configure().keys())


mainloop()
