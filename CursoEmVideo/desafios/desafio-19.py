from random import randint

nomes = ['pedro', 'maria', 'andre']
ger = randint(1, 3)

if ger == 1 :
    ger = 'maria'
elif ger == 2 :
    ger = 'pedro'
elif ger == 3 :
    ger = 'andre'
    

print('eu escolho {}'.format(ger))
