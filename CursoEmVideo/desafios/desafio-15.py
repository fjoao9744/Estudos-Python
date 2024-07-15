dia = int(input('quantos dias você alugou o carro? '))
km = int(input('quantos kilometros você rodou? '))
diar = 60
kmr = 0.15
print('você tera que pagar de aluguel R${} reais'.format((dia * diar) + (km * kmr)))