from random import randint
tabela = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('o numeros sorteados foram:', end=' ')
for c in tabela:
    print(c, end=' ')
    
print(f'\no menor numero foi o {min(tabela)}')
print(f'o maior numero foi o {max(tabela)}')
    