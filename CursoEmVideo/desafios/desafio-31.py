n1 = int(input('quantos KM você vai percorrer na sua viagem? '))

if n1 <= 200:
    print('sua passagem vai custar {} reais'.format(n1*0.50))
else:
    print('sua passagem vai custar {} reais'.format(n1*0.45))