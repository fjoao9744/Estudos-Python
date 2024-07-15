from datetime import date

n1 = int(input('qual ano você esta?, coloque 0 para pegar o atual: '))
if n1 == 0:
    n1 = date.today().year

if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('esse ano é bissexto')
else:
    print('esse ano não foi bissexto')
