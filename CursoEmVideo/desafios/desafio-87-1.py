lista = [
         [[], [], []],
         [[], [], []],
         [[], [], []]
        ]

lista_par = []
coluna_3 = []
maior_2 = 0

for l in range(3):
    for c in range(3):
        item = int(input(f"Digite um valor para {l}x{c}: "))
        lista[l][c].append(item)

        if l == 0 and c == 0:
            maior_2 = item

        if item % 2 == 0:
            lista_par.append(item)

        if c == 2:
            coluna_3.append(item)
        if l == 1:
            if item >= maior_2:
                maior_2 = item

for l in range(3):
    for c in range(3):
        print(f"[{lista[l][c][0]:^5}]", end='')
    print()

print(f"Todos os valores pares digitados foram: {lista_par} e a soma deles fica {sum(lista_par)}")
print(f"A soma de todos os valores digitados na coluna 3 foi de: {sum(coluna_3)}")
print(f"O maior numero digitado na linha 2 foi: {maior_2}")

