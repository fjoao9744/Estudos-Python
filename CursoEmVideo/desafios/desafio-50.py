n2 = 0
for c in range(1, 7):
    n1 = int(input('digite o {}° numero: '.format(c)))
    if n1 % 2 == 0:
        n2 += n1
print('a soma de todos os valores pares é de {}'.format(n2))

