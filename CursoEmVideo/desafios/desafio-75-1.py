tabela = (int(input('digite um valor: ')),
          int(input('digite um valor: ')),
          int(input('digite um valor: ')), 
          int(input('digite um valor: ')))

print(f'Você digitou {tabela}')
print(f'O valor 9 apareceu {tabela.count(9)} vezes')
if 3 in tabela:
    print(f'O valor 3 apareceu na {tabela.index(3) + 1}° posição')
else:
    print(f'O valor 3 apareceu em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for i in tabela:
    if i % 2 == 0:
        print(i, end=' ')
