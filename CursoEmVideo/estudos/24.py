nome = 'josé'
idade = 44
salario = 720.50


print(f'{nome} tem {idade} anos e ganha {salario}')
print(f'{nome} tem {idade} anos e ganha {salario:.2f}') #2 numeros dps da virgula
print(f'{nome} tem {idade:^10} anos e ganha {salario:.2f}') #idade centralizada em 10 espaços
print(f'{nome:-^10} tem {idade:^10} anos e ganha {salario:.2f}') #nome centralizado com traços em volta
print(f'{nome:<10} tem {idade:>10} anos e ganha {salario:.2f}') #nome alinhado a esquerda e idaed alinhado a direita