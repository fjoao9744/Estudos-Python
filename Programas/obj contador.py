class Contador:
    instancias = 0
    
    def __init__(self):
        Contador.instancias += 1
        
    @staticmethod
    def exibir():
        print(Contador.instancias)
        
        
cont = Contador()

cont.exibir()

cont = Contador()
cont = Contador()

cont.exibir()