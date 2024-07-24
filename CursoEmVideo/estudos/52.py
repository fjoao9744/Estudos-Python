lista = [['Joao', 20.0],
['Maria', 30.0],
['Beatriz', 10.0],
['Kauan', 30.0]]

peso = []

for c in lista:
    for i, v in enumerate(c):
        if i == 1:
            peso.append(v)

print(peso)
peso.sort()

for pessoa in lista:
    for i in peso:
        if i in c:
            print()