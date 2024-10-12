# não vamos nos aprofundar nisso agora

import tkinter as tk 
from tkinter import ttk #começamos a mostrar as funções do tk pq agora vamos usar o ttk
#ttk tem as mesmas funções do tk porem mais bonitas

tela = tk.Tk() 
frame = ttk.Frame(tela) #criamos um frame e falamos onde ele vai ficar 
frame.grid(row=3, column=0) #vamos colocar eel na 3° linha da tela

l1 = tk.Label(tela, text="linha 1").grid(row = 0, column = 0) # podemos coloca ro grid em uma só linha, só n recomendo pq pode e vai dar problemas no futuro
l2 = tk.Label(tela, text="linha 2").grid(row = 1, column = 0) # vamos criar mais uma label para mostrar uma função do ttk

l3 = ttk.Label(frame, text="linha 3").grid(row = 2, column = 0) #vamos criar um terceira label mas envez de colocar na tela normal, vamos colocar no frame

tela.mainloop() 