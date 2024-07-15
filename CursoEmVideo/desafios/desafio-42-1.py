l1 = int(input('digite o primeiro comprimento de reta: '))
l2 = int(input('digite o segundo comprimento de reta: '))
l3 = int(input('digite o terceiro comprimento de reta: '))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print('pode formar um triangulo', end='')
    if l1 == l2 == l3:
        print(' equilatero')
    if l1 != l2 and l1 != l3 and l2 != l3:
        print(' escaleno')
    else:
        print(' isósceles')
else:
    print('não pode formar um triangulo')
    