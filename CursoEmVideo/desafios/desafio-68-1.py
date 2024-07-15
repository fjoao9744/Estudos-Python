from random import randint 

vitorias = 0

while True:
    print(f'vitorias = {vitorias}')
    p_i = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]

    pc = randint(0, 10)
    player = int(input('Digite um valor: '))
    print('-'*20)
    while p_i != 'P' and p_i != "I":
        print('digite P ou I')
        player = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]

    soma = pc + player

    if p_i == 'P':
        if soma % 2 == 0:
            vitorias += 1
            print(f'você venceu! o computador jogou {pc} e você {player}, que da {soma} e é PAR \n', '-' * 20)
        if soma % 2 == 1:
            print(f'o computador jogou {pc} e você {player}, que da {soma} e é IMPAR')
            break
    if p_i == 'I':
        if soma % 2 == 1:
            vitorias += 1
            print(f'você venceu! o computador jogou que {pc} e você {player}, que da {soma} e é IMPAR \n', '-' * 20)
        if soma % 2 == 0:
            print(f'o computador jogou {pc} e você {player}, que da {soma} e é PAR')
            break


print(f'você perdeu! com {vitorias} vitorias')