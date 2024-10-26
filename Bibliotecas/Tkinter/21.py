from tkinter import *

tela = Tk()
tela.geometry("400x300")

mensagens = Listbox(tela) 
sel = Listbox(tela) 

def enviar_mensagem():
    mensagem = caixa.get() 
    mensagens.insert(END, mensagem) 

def func_tamanho():
    quant_men = mensagens.size() #size pega quantas mensagens tem no listbox
    tamanho["text"] = quant_men # mostra na tela a quantidade

tamanho = Label(tela, text='0') #criação da label pra mostrar quantas mensagens tem 
caixa = Entry(tela)
botao = Button(tela, text="Submit", command=enviar_mensagem)
botao_size = Button(tela, text="quantidade de mensagens", command=func_tamanho)





caixa.pack(side=BOTTOM)
botao.pack(side=BOTTOM)
botao_size.pack(side=BOTTOM)
tamanho.pack()
mensagens.pack(anchor=CENTER, side=RIGHT) 
mainloop()
