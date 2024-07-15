tabela = (int(input('digite um valor: ')),
          int(input('digite um valor: ')),
          int(input('digite um valor: ')), 
          int(input('digite um valor: ')))

pares = 0
for c in tabela:
    if c % 2 == 0:
        pares += 1

print(f'Você digitou {tabela}')
print(f'O valor 9 apareceu {tabela.count(9)} vezes')
try:
    print(f'O valor 3 apareceu na {tabela.index(3) + 1}° posição')
except:
    print(f'O valor 3 apareceu em nenhuma posição')
print(f'Os valores pares digitados foram: {pares} ')

