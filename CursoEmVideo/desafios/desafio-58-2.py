from random import randint

print('estou pensando em um numero de 1 a 10...')
n1 = int(input('tente advinhar: '))
n2 = randint(1, 10)
count = 1
while n1 != n2:
    count += 1
    if n1 > n2:
        n1 = int(input('menos... tente advinhar: '))
    elif n1 < n2:
        n1 = int(input('mais... tente advinhar: '))
    
print('você advinhou com {} tentativas! o numero realmente era {}'.format(count, n1))
    
    