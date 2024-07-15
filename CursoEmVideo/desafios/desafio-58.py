from random import randint 
n1 = 0
x = 11

while x != n1:
    n1 = randint(1,10)
    x = int(input('tente adivinhar o numero que eu estou pensando: '))
    print('o numero que eu pensei foi... {}'.format(n1))

print('programa encerrado')
