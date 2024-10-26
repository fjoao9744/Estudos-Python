import variaveis
import random


posição = 2
novo = 0

mapa = variaveis.mapa[:]
while True:
    mapa = variaveis.mapa[:]
    

    if novo > 0:
        for add in range(novo):
            mapa.append(random.choice(variaveis.events))


    for contador in mapa:
        
        mapa[posição] = variaveis.player

        print(contador, end='')
    print('\n')
    for contador in range(len(mapa)):
        print(f' {contador} ', end='')

    
    
    print(f'\n{'<-- A - D -->':-^40} ')
    andar = input().upper().strip()

    if andar == 'D' and variaveis.player == mapa[-1]:
        novo += 1
    elif andar == 'D':
        posição += 1

    if andar == 'A':
        posição -= 1

    mapa.clear()
    

    

    