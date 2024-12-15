class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        print(f"{self.nome} latiu")


dog = Cachorro("tobias", 12)

print(dog.nome)

dog.latir()

