try:
    n = int(input('digite um NUMERO: '))

    print(f'seu numero foi: {n}')
    
except ValueError:
    print('você não digitou um numero.')
