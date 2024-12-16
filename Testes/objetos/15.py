class Multiplicador:
    def __init__(self, num):
        self.num = num

    def __call__(self, num):
        return num * self.num

dobro = Multiplicador(2)

print(dobro(4))

triplo = Multiplicador(3)

print(triplo(2))
    
class Somador:
    def __init__(self):
        self.total = 0

    def __call__(self, *args):
        self.total += sum(args)

        return self.total

soma = Somador()

print(soma(1, 2, 3, 4, 10)) # 20

print(soma(5)) # 25 (20 + 5)

