from tkinter import *

tela = Tk()
tela.config(bg="black") 

l1 = Label(tela, text="temos um texto", padx=10, bg="blue", fg="white") # vamos criar uma label bem diferentona
l1.grid(row=0, column=0) 

texto = l1["text"] #você pode acessar as caracteristicas de um widget e altera-los como quiser

print(texto)


def mudar_texto(): #vamos criar uma função para alterar o texto 
    l1['text'] = "o texto foi mudado"
    #l1.config(text = "o texto foi mudado")
    
botao = Button(tela, text="clique aqui", command=mudar_texto).grid(row=2, column=0) #botao que altera o texto da label

mainloop()
