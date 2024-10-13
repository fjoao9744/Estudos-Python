from tkinter import *

tela = Tk()
tela.title("teste") # assim alteramos o titulo da janela
tela.geometry('500x500')

entrada = Entry(tela) #vamos criar uma caixa de entrada
entrada.grid(row= 0, column=0)

i = 0
def enviar(): #criando uma função para criar uma label na tela com oq esta escrito a entry
    global i
    dado = entrada.get() #pegando oque esta na entry
    i += 1
    l = Label(tela, text=dado) #criando a label
    l.grid(row=i, column=0)

botao = Button(tela, command=enviar, text="submit") 
botao.grid(row=0, column=1)

print(entrada.configure().keys())

mainloop()
