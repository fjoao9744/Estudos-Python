import time

n1 = int(input('digite um primeiro valor: '))
n2 = int(input('digite um segundo valor: '))

n3 = 0
menu = int(input('Oque deseja? \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] novos valores\n[5] Sair do programa\n'))

while menu != 5:
    
    if menu == 1:
        n3 = n1 + n2
        print('o resultado foi {}'.format(n3))
    if menu == 2:
        n3 = n1 * n2
        print('o resultado foi {}'.format(n3))
    if menu == 3:
        if n1 > n2:
            n3 = n1
        elif n2 > n1:
            n3 = n2
        print('o resultado foi {}'.format(n3))
    if menu == 4:
        n1 = int(input('digite um primeiro valor: '))
        n2 = int(input('digite um segundo valor: '))
    
    
    time.sleep(2)
    menu = int(input('Oque deseja? \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] novos valores\n[5] Sair do programa\n'))

print('programa encerrado')

