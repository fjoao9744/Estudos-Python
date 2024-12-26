# __new__ x __init__

class Pessoa:
    def __new__(cls): # o __new__ vem antes do __init__
        cls.smogon = 1
        
        objeto = super().__new__(cls)
        return objeto # o retorno da instancia é obrigatorio
    

joao = Pessoa()

print(joao.smogon)