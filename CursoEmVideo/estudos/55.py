import os

lista = [
         [[], [] ,[]],
         [[], [], []],
         [[], [], []] 
        ]
l = 1
c = 1
while True:

    lista[l][c] = 0

    print(f'{lista[0]} \n{lista[1]} \n{lista[2]}')
    lista = [
         [[], [] ,[]],
         [[], [], []],
         [[], [], []] 
        ]
    n = str(input('digite a direção que irá seguir:')).upper()
    if n == 'D':
        c += 1
    if n == 'B':
        l += 1
    
    if n == 'C':
        l -= 1
    if n == 'E':
        c -= 1

    os.system('cls')

