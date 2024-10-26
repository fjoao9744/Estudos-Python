n = int(input('Digite um numero para ver sua tabuada: ')) #pergunta qual o numero da tabuada
c = 0
while c != 10: #a tabuada
    c = c + 1
    print('{} x {} = {}'.format(n, c, n * c))