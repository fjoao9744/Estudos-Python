n1 = float(input('digite seu salario: '))

if n1 <= 1250:
    n2 = (15 / 100) * n1
    print('seu aumento foi de 15%, então salario agora é {}'.format(n1 + n2))

else:
    n2 = (10 / 100) * n1
    print('seu aumento foi de 10%, então salario agora é {}'.format(n1 + n2))

