#monstro
def monstro(nome, hp, atk, Def):
    
        print('''\033[0;30;40m
        Nome = {} \n
        Hp = {} \n
        Ataque = {} \n
        Defesa = {} \n 
        \033[m'''.format(nome, hp, atk, Def))

beholder = monstro('beholder', 10, 3, 1)



