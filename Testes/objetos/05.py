class Monstro:

    buff = 1.5 # esse atributo vai ser compartilhado para todos os objetos

    def __init__(self, nome, atk):
        self.nome = nome
        self.atk = atk

    @classmethod
    def mudar_buff(cls, novo_buff):
        cls.buff = novo_buff

class Slime(Monstro):
    def __init__(self, nome, atk, item="gosma"):
        super().__init__(nome, atk)

        self.__item = item # Um atributo privado

    def atacar(self):
        print(f"{self.nome} atacou")

    def dropar(self):
        print(f"{self.nome} dropou {self.__item}")

    def buffar(self):
        self.atk *= Slime.buff

    @staticmethod
    def info():
        print("isso é um monstro!")


slime_verde = Slime("slime verde", 4)
slime_azul = Slime("slime azul", 3)

print("=sem buff=")
print("slime verde: ", slime_verde.atk)
print("slime azul: ", slime_azul.atk)

slime_verde.info()

print("=Com buff(1.5)=")

slime_verde.buffar()

print("slime verde: ", slime_verde.atk)

print("=Com buff(2)=")
slime_verde.mudar_buff(2)

slime_verde.buffar()
slime_azul.buffar()

print("slime verde: ", slime_verde.atk)
print("slime azul: ", slime_azul.atk)

print("=Com buff(3)=")
slime_verde.mudar_buff(3)

slime_verde.buffar()
slime_azul.buffar()

print("slime verde: ", slime_verde.atk)
print("slime azul: ", slime_azul.atk)
