import tkinter as tk # vamos importar e trocar por tk para facilitar o entedimento futuro

tela = tk.Tk() #coloca tk antes das funções do tkinter

l1 = tk.Label(tela, text="linha 1")
l1.grid(row = 0, column = 0)

print(l1.configure().keys()) # ve as caracteristicas do l1

l1.config(padx = 50) #aumenta o padding x em 50 do l1

tela.mainloop() #coloca qual tela vc vai querer rodar