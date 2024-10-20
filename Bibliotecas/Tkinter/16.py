from tkinter import *

tela = Tk()

def desligar(): # função que vai desativar ou ativar o botão
    if botao["state"] == NORMAL: #verifica se o botão ta ligado ou desligado, é pra isso que o state serve
        botao["state"] = DISABLED
        botao["text"] = "desativado"

botao = Button(tela, text="ativado", fg="green", command=desligar) #criando um botão de ativado
botao.pack()

mainloop()