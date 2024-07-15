print('{:=^40}'.format('LOJAS DO SMOGON'))
preço = float(input('qual o valor do produto que deseja pagar?'))

print('qual vai ser a forma de pagamento?')
num = int(input('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
qual é a opção?'''))

if num == 1:
    preço = preço - (preço*10)//100
    print('seu produto custará R${} reais á vista'.format(preço))
elif num == 2:
    preço = preço - (preço*5)//100
    print('seu produto custará R${} reais á vista no cartão'.format(preço))
elif num == 3:
    preço = preço // 2
    print('seu prouto custará R${} reais de 2x no cartão'.format(preço))
elif num == 4:
    juros = (preço*20)// 100
    par = int(input('em quantas vezes você vai parcelar?'))
    preço = preço // par + juros
    print('seu produto custara R${} reais parcelado de {}x no cartão'.format(preço, par))
else:
    print('opção invalida!! tente novamente!')

