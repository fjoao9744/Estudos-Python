expressão = list(input('digite uma expressão '))
lista = []
for c in expressão:
    if c == '(':
        lista.append('(')

    elif c == ')':
        lista.append(')')

print('é valida' if lista[-1] == '(' else 'é invalida')

