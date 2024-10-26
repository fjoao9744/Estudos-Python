from tkinter import *

tela = Tk()
tela.geometry("400x300")

mensagens = Listbox(tela) #criação da listbox
sel = Listbox(tela) #criando outro listbox

def enviar_mensagem():
    mensagem = caixa.get() 
    mensagens.insert(END, mensagem) 

def selecionar_mensagem():
    mensagem_sel = mensagens.get(END) #pega o oque esta no index get(index1, index2)
    sel.insert(END, mensagem_sel) 




caixa = Entry(tela)
botao = Button(tela, text="Submit", command=enviar_mensagem)
botao_sel = Button(tela, text="Selecionar", command=selecionar_mensagem) #botao para pegar o ultimo e adicionar na outra listbox




caixa.pack(side=BOTTOM)
botao.pack(side=BOTTOM)
botao_sel.pack(side=BOTTOM)
mensagens.pack(anchor=CENTER, side=RIGHT) 
sel.pack(anchor=CENTER, side=LEFT)
mainloop()
