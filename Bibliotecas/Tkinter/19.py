from tkinter import *
# vou usar o mesmo do outro pra ensinar mais coisas

tela = Tk()
tela.geometry("400x300")

mensagens = Listbox(tela)


def enviar_mensagem():
    mensagem = caixa.get() 
    mensagens.insert(END, mensagem) 

def deletar_mensagem():
    mensagens.delete(END) # metodo delete(index)


caixa = Entry(tela)
botao = Button(tela, text="Enviar", command=enviar_mensagem) #alterei os nomes
botao_del = Button(tela, text="Deletar", command=deletar_mensagem)



caixa.pack(side=BOTTOM, fill=BOTH) #o fill serve para falar se o widget vai preencher, BOTH é ambos os lados, mas ele tmabema ceita X ou Y
botao.pack(side=BOTTOM, fill=BOTH)
botao_del.pack(side=BOTTOM, fill=BOTH)

mensagens.pack() 

mainloop()
