import random

#title
print('\033[1;30;40m-----RPG GAME V1-----\033[m')

#variaveis
Nome = str(input('para começar, digite seu nome: '))
Hp = 20
Atk = 2
Def = 0
Andar = 0

cond = [1, 2, 3]

print(f'''\033[0;30;40m
Nome = {Nome} \n
Hp = {Hp} \n
Ataque = {Atk} \n
Defesa = {Def} \n
Andar = {Andar} \n
\033[m''')


print('\033[1;30;40m-----[Afinal, como vai funcionar o jogo?]----- \nvocê vai ter que entrar em 3 masmorras que vão ter perigos aleatorios\033[0;30;40m')
n1 = str(input('esta pronto?[S/N]')).strip().upper()
if n1 == 'S':
        print('otimo!')
if n1 == 'N':
        print('que bom :)')


#andar 1
Andar = 1
cond1 = random.choice(cond)
cond.remove(cond1)

print('\033[0;30;40m-----PRIMEIRO ANDAR-----\033[m')

if cond1 == 1:
        print('você percorre por todo o andar da dungeon \n porem você não acha nada...')
elif cond1 == 2:
        print('você achou uma reliquia que aumenta seu hp')


#andar 2
Andar += 1
cond1 = random.choice(cond)
cond.remove(cond1)
print('\033[0;30;40m-----SEGUNDO ANDAR-----\033[m')












