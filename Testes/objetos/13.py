class World:
    def __init__(self):
        self.fase = 0

    def __next__(self):
        self.fase += 1

mundo = World()

print(mundo.fase)

next(mundo)

print(mundo.fase)

print("-" * 40)
class Contador:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual >= self.fim:
            raise StopIteration  # Levanta exceção quando a iteração termina

        self.atual += 1
        return self.atual - 1

cont = Contador(1, 5)

for _ in cont:
    print(_)


