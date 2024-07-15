casa = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Por quantos anos você vai querer pagar pela casa? '))
valor = (casa//anos) // 12

print('se o valor da casa é de R${} e você vai querer pagar por {} anos, ficara R${} reais por mês'.format(casa, anos, valor))
if (salario*30) // 100 <= valor:
    print('lamento, a sua compra não podera ser efetuada.')
else:
    print('a sua compra podera ser efetuada.')


'''if (salario*30)//100 < (casa // anos)//12 :
    print('lamento, mas você não podera financiar uma casa com esse custo.')
elif (salario*30)//100 > (casa // anos)//12:
    print('pois bem, casa custara {} por mes.'.format((casa // anos)//12))'''
