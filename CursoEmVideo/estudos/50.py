lista1 = []
lista2 = []

for c in range(0, 3):
    lista2.append(str(input('Digite seu nome: ')))
    lista2.append(int(input('Digite sua idade: ')))
    lista1.append(lista2)
    lista2 = []

print(lista1)