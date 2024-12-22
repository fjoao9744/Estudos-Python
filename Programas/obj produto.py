class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    def desconto(self, desconto):
        desconto = self._preco * desconto // 100
        
        self._preco = self._preco - desconto
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
        
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        print("O nome foi alterado")
        
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco
        print("O preco foi alterado!")
        
    
carro = Produto("carro", 100)

print(carro.nome, carro.preco)

carro.desconto(20)

print(carro.nome, carro.preco)

carro.nome = "corsa"

print(carro.nome, carro.preco)

carro.preco = 200

print(carro.nome, carro.preco)

carro.desconto(80)

print(carro.nome, carro.preco)

