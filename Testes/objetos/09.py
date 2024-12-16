class Animal:
    def __init__(self, nome):
        self.nome = nome

    def __add__(self, other):
        return Animal(self.nome + other.nome)


zumbi = Animal("zumbi ")
cavalo = Animal("cavalo ")

cavalo_zumbi = cavalo + zumbi

print(cavalo_zumbi.nome)

