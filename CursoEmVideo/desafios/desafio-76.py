listagem = ('lapis', 1.10, 'borracha', 2.20, 'apontador', 4.00, 'trasferidor', 8.00, 'estojo', 6.50)

print(f'{'-' * 30}\n{'LISTAGEM DE PREÇOS':^30}\n{'-' * 30}')

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<20}', end='')
    else:
        print(f'R${listagem[c]:.2f}')
print('-' * 30)
    
