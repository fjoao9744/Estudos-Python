from random import randint
tabela = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('o numeros sorteados foram:', end=' ')
for c in tabela:
    print(c, end=' ')
    
print(end='\n')
tabela_sorteada = sorted(tabela)

print(f'o menor numero foi o {tabela_sorteada[0]}')
print(f'o maior numero foi o {tabela_sorteada[-1]}')
    



