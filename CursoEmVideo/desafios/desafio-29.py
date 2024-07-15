n1 = int(input('quantos KM/h você estava? '))

if n1 > 80:
    print('você foi multado!')
    print('sua multa foi de {} reais'.format((n1-80)*7))

else:
    print('tudo certo!')