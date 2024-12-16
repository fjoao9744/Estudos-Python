class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, other):
        if isinstance(other, Pessoa): # O objeto é da classe pessoa?
            return self.idade == other.idade

        return False

joao = Pessoa("joao", 22)
maria = Pessoa("maria", 22)
jorge = Pessoa("jorge", 25)

print(joao == maria) # True pq eles tem a mesma idade
print(joao == jorge) # False pq eles tem idades diferentes
