idade = int(input('digite a idade do nadador: '))

if idade <= 9:
    print('nadador mirim')
elif idade <= 14:
    print('nadador infantil')
elif idade <= 19:
    print('nadador junior')
elif idade == 20:
    print('nadador senior')
else:
    print('nadador master')