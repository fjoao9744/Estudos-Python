class Pessoa:
    especie = "humano" # atributo da classe

    def __init__(self, nome):
        self.nome = nome # atributo de instancia

p1 = Pessoa("joao")
p2 = Pessoa("maria")

print(p1.nome, p1.especie)
print(p2.nome, p2.especie)

Pessoa.especie = "Smogon"

print(p1.nome, p1.especie)
print(p2.nome, p2.especie)