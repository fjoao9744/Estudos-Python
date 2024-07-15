from random import randint

nt = randint(0, 5)
nf = int(input('tente advinhar o numero que o computador escolheu: '))

if nf == nt:
    print('você advinhou!')
else:
    print('você errou, era {}'.format(nt))
