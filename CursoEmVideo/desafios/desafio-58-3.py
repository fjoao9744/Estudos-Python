from random import randint
pc = randint(1, 10)

print('estou pensando em um numero de 1 a 10...')
n1 = int(input('tente advinhar: '))
fim = False
count = 1
while fim == False:
    
    
    if n1 == pc:
        fim = True
    else:
        if n1 > pc:
            n1 = int(input('menos... tente advinhar: '))
            
        elif n1 < pc:
            n1 = int(input('mais... tente advinhar: '))
        count += 1

print('você advinhou com {} tentativas! o numero realmente era {}'.format(count, n1))
    
    