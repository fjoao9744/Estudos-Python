expressão = list(input('digite uma expressão '))
valida = True
parenteses = 0
for cont in expressão:
    if cont == '(':
        parenteses += 1
    elif parenteses == 1 and cont == ')':
        parenteses = 0

if parenteses == 1:
        valida = False

while ' ' in expressão:
    expressão.remove(' ')

print(f'a expressão {expressão} é... ', end='')
if valida == True:
    print('valida!')
if valida == False:
    print('invalida!')


    