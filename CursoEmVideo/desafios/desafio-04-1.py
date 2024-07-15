o = input('digite algo ')
print('é um numero? {}'.format(o.isnumeric()))
print('tem letras? {}'.format(o.isalpha()))
print('tem letras e/ou numeros? {}'.format(o.isalnum()))
print('tem letras minusculas e maiusculas? {}'.format(o.istitle()))
print('todas as letras são minusculas? {}'.format(o.islower()))
print('todas as letras são maiusculas? {}'.format(o.isupper()))
print('é um espaço? {}'.format(o.isspace()))

