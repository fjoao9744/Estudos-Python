

class Tarefas:
    def __init__(self):
        self.lista = dict()
        
    def adicionar(self, tarefa):
        if tarefa in self.lista:
            print("a tarefa ja esta existe")
            return
        self.lista[tarefa] = "❌"
        
    def concluir(self):
        for k, v in self.lista.items():
            print(f"{k} {v}")
            
        tarefa = str(input("Qual tarefa você deseja concluir? ")) 
        if tarefa not in self.lista:
            print("A tarefa não existe.")
            return
        self.lista[tarefa] = "✅"
    
    def __call__(self):
        for k, v in self.lista.items():
            print(f"{k} {v}")
            
l = Tarefas()
l.adicionar("usar smogon")
l.adicionar("usar smogon")

l.concluir()

l()