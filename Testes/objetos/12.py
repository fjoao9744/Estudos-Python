class Player:
    def __init__(self, nome, itens = []):
        self.nome = nome
        self.itens = list(itens)

    def __iter__(self):
        return iter(self.itens)

    def add_item(self, item):
        self.itens.append(item)


joao = Player("João")

joao.add_item("arma")
joao.add_item("escudo")

for _ in joao:
    print(_)

# __next__

