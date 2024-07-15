_ = '-' * 20

mulher_menor_20 = 0
pessoas_maior = 0
homens = 0

count = 0
sexo = ' '


while True:
    print(f'{_}\nCADASTRE UMA PESSOA\n{_}')
    idade = int(input('qual a idade? '))
    continuar = sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o sexo? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input(f'{_}\nquer continuar?[S/N] ')).strip().upper()[0]

    if sexo == "F" and idade < 20:
        mulher_menor_20 += 1
    if idade >= 18:
        pessoas_maior += 1
    if sexo == 'M':
        homens += 1


    
    if continuar == 'N':
        break
    
print(f'pessoas com mais de 18: {pessoas_maior}')
print(f'quantidade de homens: {homens}')
print(f'mulheres com menos de 20: {mulher_menor_20}')