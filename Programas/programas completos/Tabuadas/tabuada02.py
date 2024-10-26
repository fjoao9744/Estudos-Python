n = int(input('Digite um numero para ver sua tabuada: ')) #pergunta qual o numero da tabuada

for c in range(1, 11): #a tabuada
    print('{} x {} = {}'.format(n, c, n * c))