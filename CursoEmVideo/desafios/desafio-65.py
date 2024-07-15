n1 = n2 = 0
med = 0
count = 0
fim = False

maior = 0
menor = 0

while fim == False:
    
    n1 = int(input('digite um numero(caso queira parar, digite 0): '))
    n2 += n1 

    if count == 0:
        menor = n1

    if n1 > maior:
        maior = n1
    elif n1 < menor and n1 != 0:
        menor = n1

    if n1 == 0:
        med = n2 / count
        fim = True

    count += 1
    print(n1, n2, count, menor, maior)

print('a media entre os numeros é de {:.2f}, o menor é {} e o maior é {}'.format(med, menor, maior))


    