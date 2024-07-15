n1 = int(input('digite um numero inteiro:'))
print('''selecione uma opção:
    [1] binario
    [2] octal
    [3] hexa''')
opção = int(input('qual opção você escolhe?'))

if opção == 1:
    print('seu valor para binario é {}'.format(bin(n1)[2:]))
elif opção == 2:
    print('seu valor para octal é {}'.format(oct(n1)[2:]))
elif opção == 3:
    print('seu valor para hexa é {}'.format(hex(n1)[2:]))
else:
    print('opção invalida')