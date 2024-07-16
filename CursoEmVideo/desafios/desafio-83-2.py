expressão = list(input('digite uma expressão '))
lista = []

for c in expressão:
    if c == '(':
        lista.append('(')
        
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('sua expressão é valida')
else:
    print('sua expressão é invalida')

    