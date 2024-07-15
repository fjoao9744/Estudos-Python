times = ('Flamengo' , 'Botafogo', 'Bahia', 'Palmeiras', 'Cruzeiro',
        'Athletico-PR', 'Bragantino' , 'São Paulo' , 'Internacional',
        'Atlético-MG', 'Fortaleza', 'Juventude', 'Cuiabá', 'Criciúma' ,
        'Vitória', 'Vasco da Gama', 'Atlético' , 'Corinthians', 'Grêmio',
        'Fluminense')

print(f'{'-'* 10} TABELA DO BRASILEIRÃO {'-' * 10}')
print(f'LISTA DE TIMES: \n{times}')
print(f'\nTOP5: \n{times[0:5]}')
print(f'\nOS 4 ULTIMOS: \n{times[-4:]}')
print(f'\nTIMES EM ORDEM ALFABETICA: \n{sorted(times)}')
print(f'\nQUAL A POSIÇÃO DO CRICIÚMA? \n{times.index('Criciúma') +1}°')
