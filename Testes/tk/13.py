import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.configure('TButton', background='blue', foreground='red')

style.theme_use('clam')  # Pode ser 'default', 'clam', 'alt', 'classic', etc.

# Exemplo de uso de widgets
label = ttk.Label(root, text="Usando o tema clam")
botao = ttk.Button(root, text="smogon")
botao.pack()
label.pack(pady=10)

root.mainloop()