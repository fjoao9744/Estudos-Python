import random

monstros = []
def monstro():
    status = {
        'nome':f'monstro{random.randint(1,10)}'
    }
    monstros.append(status)

print()