numero = int(input('Digite um numero para ver sua tabuada: ')) #pergunta qual o numero da tabuada
contador = 0
while True:
    contador += 1
    print(f'{numero} x {contador} = {numero * contador}') #a tabuada
    if contador == 10: #para a tabuada
        break