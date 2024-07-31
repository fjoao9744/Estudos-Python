from random import choice
from time import sleep


lista = tuple(range(60))
numero = []

print('=' * 20)
print('JOGUE NA MEGA SENA')
print('=' * 20)

quant = int(input('quantos jogos você quer que eu sorteie?  '))
print('=' * 5,f'SORTEANDO {quant} JOGOS...', '=' * 5)
for i in range(1, quant + 1):
    print(f'jogo {i}: ', end=' ')
    for c in range(0, 6):
        numero.append(choice(lista))
    print(sorted(numero))
    numero.clear()
    sleep(1)
        
print(f'{' BOA SORTE ':=^20}')

