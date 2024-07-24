lista = [[], []]

for c in range(1, 8):
    n = int(input(f'digite o {c}° numero: '))
    lista[0].append(n) if n % 2 == 0 else lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(f'os valores pares digitados foram: {lista[0]} \nos valores impares digitados foram: {lista[1]}')
