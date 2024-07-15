preco = float(input('digite um preço '))
aumento = int(input('digite o aumento '))
r = (preco*aumento / 100) + preco
print('o valor R${} com {}% de aumento fica {:.3f}'.format(preco, aumento, r))