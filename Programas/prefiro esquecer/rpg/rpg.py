import random
import time

print('\033[1;30;40m-----RPG GAME V1-----\033[m')

time.sleep(2)

Nome = str(input('para começar, digite seu nome: '))
Hp = 20
Atk = 2
Def = 0

player = {'nome':Nome, 'hp':Hp, 'atk':Atk, 'def':Def}
Andar = 0

time.sleep(1)

def player1(nome, hp, atk, Def, andar):
    
        print('''\033[0;30;40m
        Nome = {} \n
        Hp = {} \n
        Ataque = {} \n
        Defesa = {} \n
        Andar = {} \n
        \033[m'''.format(nome, hp, atk, Def, andar))
    
    
player1(player['nome'], player['hp'], player['atk'], player['def'], Andar)

time.sleep(1)

print('\033[1;30;40m-----[Afinal, como vai funcionar o jogo?]----- \nvocê vai ter que entrar em 3 masmorras que vão ter perigos aleatorios\033[0;30;40m')
n1 = str(input('esta pronto?[S/N]')).strip().upper()
if n1 == 'S':
        print('otimo!')
if n1 == 'N':
        print('que bom :)')
time.sleep(2)


Andar = 1
print('\033[0;30;40m-----PRIMEIRO ANDAR-----\033[m')
