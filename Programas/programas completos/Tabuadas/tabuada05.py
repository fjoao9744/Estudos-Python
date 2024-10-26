numero = int(input('Digite um numero para ver sua tabuada: ')) #pergunta qual o numero da tabuada
contador = 0
while True:
    contador += 1
    print(f'{numero:2} + {contador:2} = {numero + contador:2}', end=' | ') # a tabuada
    print(f'{numero:2} - {contador:2} = {numero - contador:2}', end=' | ')
    print(f'{numero:2} * {contador:2} = {numero * contador:2}', end=' | ')
    print(f'{numero:2} / {contador:2} = {numero / contador:.2f}')

    if contador == 10: #para a tabuada
        break