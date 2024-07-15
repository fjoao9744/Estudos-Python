
print('\033[1m=' * 10 , 'Por favor informe seus dados' , '=\033[0;0m' * 10) #deixar bonito
nome = str(input('qual o seu nome? ')).strip()    #inputs iniciais 
sexo = str(input('qual o seu sexo?[F/M] ')).upper()
ano = int(input('qual ano você nasceu?'))
idade = 2024 - ano

palsex = ''
palcasado = 'solteiro(a)'

casado = trab = ''  #variaveis que serão usadas
medfil2 = medfil = sal = filho = alis = 0

if sexo == 'M':
    palsex = 'um homem'
    palsex = 'uma mulher'

if idade >= 18: #maior de idade
    trab = str(input('você trabalha?[S/N] ')).upper() 
    if trab == 'S':
        sal = float(input('quanto você ganha?'))
    casado = str(input('você é casado(a)[S/N]? ')).upper()
    if casado == 'S':
        palcasado = 'casado(a)'
        filho = int(input('quantos filhos você tem? '))
        if filho >= 2:
            for f in range(1, filho + 1):
                medfil = int(input('qual a idade do seu {}º filho?'.format(f)))
                medfil2 += medfil

print('ok, {} você é {} de {} anos de idade {}, tem {} filhos e ganha R${} reais'.format(nome, palsex, idade, filho, sal))
                

if idade < 18 and sexo == 'M': #menor de idade
    alis = 18 - idade



