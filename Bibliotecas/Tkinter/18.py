from tkinter import *

tela = Tk()
tela.geometry("400x300")

mensagens = Listbox(tela) #criação da listbox


def enviar_mensagem():
    mensagem = caixa.get() #pegando oque ta escrito
    mensagens.insert(END, mensagem) #inserindo oque esta escrito dentro da listbox
    # coloca o END para adicionar no final da listbox


caixa = Entry(tela)
botao = Button(tela, text="Submit", command=enviar_mensagem)




#vou começar a colocar os metodos geometricos no final para facilitar a leitura
caixa.pack(side=BOTTOM)
botao.pack(side=BOTTOM)
mensagens.pack() 

mainloop()
