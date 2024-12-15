class Monstro:
    def __init__(self, nome):
        self.nome = nome

class Slime(Monstro):
    def __init__(self, nome, item="gosma"):
        super().__init__(nome)

        self.__item = item # Um atributo privado

    def atacar(self):
        print(f"{self.nome} atacou")

    def dropar(self):
        print(f"{self.nome} dropou {self.__item}")


slime_verde = Slime("slime verde")

print(slime_verde.nome)

slime_verde.atacar()

slime_verde.dropar()

