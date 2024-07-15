salario = float(input('quanto você ganha '))
aumento = int(input('qual o seu aumento '))
print('se voce ganha R${:.2f} e recebe {}% de aumento, você passa a ganhar {:.2f}'.format(salario, aumento, (salario*aumento / 100) + salario))