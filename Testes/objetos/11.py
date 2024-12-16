class Player:
    def __init__(self, nome, itens = []):
        self.nome = nome
        self.itens = list(itens)

    def __len__(self):
        return len(self.itens)

    def __getitem__(self, indice): # permite que o item seja indexado
        return self.itens[indice]
    
    def __setitem__(self, indice, valor):
        self.itens[indice] = valor

    def add_item(self, item):
        self.itens.append(item)

joao = Player("João")

print(joao.itens)

joao.add_item("arma")

print(joao.itens)

joao.add_item("escudo")

print(joao.itens)

print(len(joao)) # __len__

print(joao[0], joao[1]) # __getitem__

joao[0] = "smogon"

print(joao[0], joao[1]) # __setitem__
