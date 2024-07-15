mais_1000 = 0
total = 0
mais_barato2 = ''
mais_barato1 = 0

c = 0
while True:
    produto = str(input('Qual o nome do produto? ')).strip().capitalize()
    preço = float(input('Qual o preço do produto?' ))

    total += preço
    if c == 0:
        mais_barato1 = preço
        c += 1
    if mais_barato1 >= preço:
        mais_barato1 = preço
        mais_barato2 = produto
        
    if preço > 1000:
        mais_1000 += 1
    
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print(f'preço total: {total}')
print(f'item mais barato: {mais_barato2}')
print(f'itens que custam mais que 1000: {mais_1000}')
