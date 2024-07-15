n1 = int(input('digite um numero: '))
n2 = int(input('digite um segundo numero '))

if n1 > n2:
    print('o maior numero é {} \ne o menor é {}'.format(n1, n2))
elif n1 < n2:
    print('o maior numero é {} \ne o menor é {}'.format(n2, n1))
else:
    print('os numeros são iguais')
