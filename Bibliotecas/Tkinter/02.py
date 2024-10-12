from tkinter import * 
tela = Tk() 

l1 = Label(tela, text="linha 1") #cria uma linha de texto
l1.grid(row=0, column=0) #posiciona ela

botao = Button(tela, text="botao") #cria um botão
botao.grid(row=1, column=0) #posiciona ele


mainloop() 