lista = [
         [[], [], []],
         [[], [], []],
         [[], [], []]
        ]

pares = 0
coluna_3 = 0
maior_2 = 0


for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = (int(input(f'digite um valor para a posição {l, c}: ')))
        if lista[l][c] % 2 == 0:
            pares += lista[l][c]
        if c == 2:
            coluna_3 += lista[l][c]
        if l == 1:
            if c == 0:
                maior_2 = lista[l][c]
            else:
                if lista[l][c] >= maior_2:
                    maior_2 = lista[l][c]

        


print(f'{lista[0][:]} \n{lista[1][:]} \n{lista[2][:]}')
print('-' * 20)
print(f'a soma dos valores pares foi de {pares}')
print(f'a soma dos valores da 3° coluna foi de {coluna_3}')
print(f'e o maior valor da linha 2 é {maior_2}')

