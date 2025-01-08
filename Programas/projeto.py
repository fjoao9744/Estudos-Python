# 22:15 - 22:58 (feito em 43 minutos)

import tkinter as tk
from random import randint

class tela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.numero = randint(0, 100)
        self.geometry("300x300")
        
        titulo = tk.Label(self, text="Tente advinhar um numero de 0 a 100").pack(pady=(30, 0))
        
        self.tentativa = tk.Entry(self)
        self.tentativa.bind("<Return>", self.tentar)
        
        self.vzs = 0
        self.label_vzs = tk.Label(self, text=f"Numero de tentativas: {self.vzs}")
        self.label_vzs.place(x=0, y=0)
        
        self.mostrar_dicas = tk.Button(self, text="Dica", command=self.dicas).pack()
        
        self.resposta = tk.Label(self, text= "")
        
        self.flag_dica = True
        
    def __call__(self):
        if self.tentativa == self.numero:
            self.resposta["text"] = "Você acertou o numero!!!!"
        
        self.tentativa.pack()
        self.resposta.pack()
        self.mainloop()
        
    def tentar(self, event=None):
        # sair
        if self.tentativa.get().lower() == "sair":
            self.destroy()
        # tratamento
        self.resposta["text"] = ""
        tentativa = self.tentativa.get().strip()
        if not tentativa.isdigit():
            self.resposta["text"] = "Digite um numero!"
            return            
        if int(tentativa) not in range(0, 100):
            self.resposta["text"] = "O numero tem que ser de 0 a 100"
            return
            
        # respostas
        if int(tentativa) == self.numero:
            self.resposta["text"] = "Resposta correta!"
            self.ganhar()
        else:
            self.resposta["text"] = "Resposta errada."
            self.vzs += 1
            self.label_vzs = tk.Label(self, text=f"Numero de tentativas: {self.vzs}").place(x = 0, y = 0)
            
            if int(tentativa) in range(int(self.numero) - 5, int(self.numero) + 5):
                self.resposta["text"] = "O numero esta perto!"
                
    def ganhar(self):
        self.tentativa["state"] = "disabled"
        self.resposta.config(fg="green")
        self.resposta["text"] = "você ganhou!!"
            
    def dicas(self):
        
        dica = "Não tem dica para achar esse numero."
        
        if self.numero % 3 == 0:
            dica = "O numero é divisivel por 3"
        if self.numero % 2 == 0:
            dica = "O numero é divisivel por 2"
        
        
        if self.flag_dica:
            self.dica = tk.Label(self, text=f"{dica}").pack()
            self.flag_dica = False
            return
        
t = tela()
t()