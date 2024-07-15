
n, n1, n2, count = int(input('digite um numero para ver o seu fatorial: ')), 1, 1, 0


while n != count or n > count:
    count += 1
    
    n1 *= n2
    n2 += 1

    
print('o fatorial de {} é {}'.format(n, n1))
