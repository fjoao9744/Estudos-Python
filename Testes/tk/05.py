import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
frame = ttk.Frame(screen, padding=10) #criando um frame, uma aba na tela separada
frame.grid()


l1 = tk.Label(frame, text="smogon1").grid(row=0, column=0)
l2 = tk.Label(frame, text="smogon1").grid(row=1, column=0)

l3 = tk.Label(screen, text="smogon3").grid(row = 2, column=0)





screen.mainloop()
