cont = 'S'
med = count = maior = menor = 0


while cont == 'S':
    n = int(input('digite um valor: '))
    med += n

    if count == 0:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

    count += 1
    

    cont = str(input('deseja continuar?[S/N]')).strip().upper()[0]
        
med = med // count
print(f'a media entre os numeros digitados foi de {med}, e o menor foi {menor} e o maior foi {maior}')

