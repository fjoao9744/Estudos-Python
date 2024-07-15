while True:
    num = int(input('quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('=' * 40, '\nA tabuada do numero solicitado é: ')
    for x in range(1, 11):
        print(f'{num} x {x} = {num * x}')
    print('=' * 40)

print('programa encerrado')
