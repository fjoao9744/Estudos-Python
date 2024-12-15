class Smogon:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Você esta printando essa classe"

    def __repr__(self):
        return "Você esta me printando em um console de debug"

hendrick = Smogon("hendrick")

print(hendrick)
print(repr(hendrick))