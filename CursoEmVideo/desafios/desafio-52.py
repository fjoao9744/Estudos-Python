n1 = int(input('digite um numero: '))
tot = 0

for c in range(1, n1+1):
    if (n1 % c) == 0:
        print('\033[0;32;40m{}\033[m'.format(c), end=' ')
        tot += 1

    else:
        print('\033[0;31;40m{}\033[m'.format(c), end=' ')
    
print('\no numero {} foi divisivel {} vezes'.format(n1, tot),end=' ')
if tot == 2:
    print('e o numero é PRIMO')
else:
    print('e ele NÃO é PRIMO')
