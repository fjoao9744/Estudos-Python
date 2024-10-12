from tkinter import * 
tela = Tk() 
tela.geometry("300x300") #aumenta o tamanho da tela



i = 0 #criando uma variavel para a label
def up() -> None: #função para quando o botao for apertado
    global i
    i += 1


    l1 = Label(tela, text=f"linha {i}") #coloca uma f string e refaz a label
    l1.grid(row=0, column=0) 



botao = Button(tela, text="botao", command=up) #colocando o parametro command para quando o botao for apertado rodar a funcao
botao.grid(row=1, column=0) 


mainloop() 