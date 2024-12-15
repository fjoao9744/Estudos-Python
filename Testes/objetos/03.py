class Monstro:
    def __init__(self, nome):
        self.nome = nome

class Slime(Monstro):
    def atacar(self):
        print(f"{self.nome} atacou")

slime_verde = Slime("slime verde")

print(slime_verde.nome)

slime_verde.atacar()

