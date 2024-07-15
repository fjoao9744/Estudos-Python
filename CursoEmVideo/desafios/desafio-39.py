from datetime import date
sexo = str(input('você é um homem ou uma mulher?'))
idade =  date.today().year - int(input('em que ano você nasceu? ' )) 

if idade == 18 and sexo == 'homem':
    print('você tera que se alistar no exercito esse ano! ')
elif idade < 18 and sexo == 'homem':
    print('voce tem {} anos para ter que alistar no exercito'.format(18 - idade))
elif idade > 18 and sexo == 'homem':
    print('você ja devia ter se alistado no exercito, ja se passaram {} anos!'.format(idade - 18))
else:
    print('você não precisa fazer o alistamento militar obrigatorio.')