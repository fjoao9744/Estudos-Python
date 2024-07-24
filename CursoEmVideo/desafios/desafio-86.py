lista = [
         [[], [], []],
         [[], [], []],
         [[], [], []]
        ]

for c in range(0, 3):
    for i in range(0, 3):
        lista[i][c] = int(input(f'digite um valor para a posição {c, i}'))
        


print(f'{lista[0][0:3]} \n{lista[1][0:3]} \n{lista[2][0:3]}')

