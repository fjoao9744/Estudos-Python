import tkinter as tk

class Screen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, text="isto é um botão", command= lambda: self.smogon.pack())
        self.smogon = tk.Label(self, text="smogon")
        self.smogon.pack_forget()
        
    def __call__(self):
        self.button.pack()
        self.mainloop()
        
tela = Screen()
tela()
