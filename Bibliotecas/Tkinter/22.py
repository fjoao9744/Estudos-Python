from tkinter import *

tela = Tk()
tela.geometry("400x300")

mensagens = Listbox(tela, selectmode=EXTENDED) 

'''
SINGLE = uma seleção por vez
BROWSE = uma seleção por vez mas aceita mecher com as setinhas
MULTIPLE = varias seleções por vez
EXTENDED = uma seleção por vez mas aceita o ctrl e o shift

'''
def enviar_mensagem():
    mensagem = caixa.get() 
    mensagens.insert(END, mensagem) 
    

caixa = Entry(tela)
botao = Button(tela, text="Submit", command=enviar_mensagem)



caixa.pack(side=BOTTOM)
botao.pack(side=BOTTOM)
mensagens.pack() 

mainloop()
