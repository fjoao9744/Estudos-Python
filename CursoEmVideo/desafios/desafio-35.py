r1 = int(input('digite o primeiro comprimento de uma reta: '))
r2 = int(input('digite o segundo comprimento de uma reta: '))
r3 = int(input('digite o terceiro comprimento de uma reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('pode formar um triangulo')
else:
    print('não pode formar um triângulo')
    