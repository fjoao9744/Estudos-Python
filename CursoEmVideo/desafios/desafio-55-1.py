maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('qual o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('o maior peso é de {}kg e o menor é {}kg'.format(maior, menor))
         
