l1 = int(input('digite o primeiro comprimento de reta: '))
l2 = int(input('digite o segundo comprimento de reta: '))
l3 = int(input('digite o terceiro comprimento de reta: '))
triangulo = False

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    triangulo = True
    print('pode formar um triangulo'.format())
else:
    print('não pode formar um triangulo')


if triangulo == True:
    if l1 == l2 == l3:
        print('e um triangulo equilatero')
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('e um triangulo isósceles')
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('e um triangulo escaleno')
