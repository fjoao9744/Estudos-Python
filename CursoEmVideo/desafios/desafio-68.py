from random import randint


vitorias = 0

while True:
    print(f'vitorias = {vitorias}')
    play = str(input('par ou impar?[P/I]')).upper().strip()[0]
    num = int(input('digite um numero de 1 a 10: '))
    pc = randint(1, 10)
    ganhador = pc + num
    if play == 'P':
        if ganhador % 2 == 0:
            print(f'você ganhou! o computador jogou {pc} e você {num}, {pc} + {num} = {ganhador} que é PAR!')
            vitorias += 1
        if ganhador % 2 == 1:
            print(f'você perdeu! o computador jogou {pc} e você {num}, {pc} + {num} = {ganhador} que é IMPAR!')
            vitorias = 0
            break
    if play == 'I':
        if ganhador % 2 == 1:
            print(f'você ganhou! o computador jogou {pc} e você {num}, {pc} + {num} = {ganhador} que é IMPAR!')
            vitorias += 1
        if ganhador % 2 == 0:
            print(f'você perdeu! o computador jogou {pc} e você {num}, {pc} + {num} = {ganhador} que é PAR!')
            vitorias = 0
            break
