valor = float(input('digite um valor '))
p = int(input('digite o imposto '))
r1 = (valor * p) / 100
r2 = valor - r1
print('algo que custa R%{} com {}% de imposto, fica R%{}'.format(valor, p, r2))
