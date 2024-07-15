valor = int(input('quanto você vai querer sacar? '))
cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

while (valor - 50) >= 0:
    cedula_50 += 1
    valor -= 50
if cedula_50 >= 1:
    print(f'total de cedulas de R$50: {cedula_50}')


while (valor - 20) >= 0:
    cedula_20 += 1
    valor -= 20
if cedula_20 >= 1:
    print(f'total de cedulas de R$20: {cedula_20}')


while (valor - 10) >= 0:
    cedula_10 += 1
    valor -= 10
if cedula_10 >= 1:
    print(f'total de cedulas de R$10: {cedula_10}')


while (valor - 1) >= 0:
    cedula_1 += 1
    valor -= 1
if cedula_1 >= 1:
    print(f'total de cedular de R$1: {cedula_1}')


