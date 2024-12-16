class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return 3.14 * (self.raio ** 2)

bola = Circulo(7)

print(bola.raio)
print(bola.area)


