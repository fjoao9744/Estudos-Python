'''pão = 1
doce = 2
bolo = 3

s = pão + doce + bolo

if s >= 150:
    print('você recebeu um bolo!)
elif s >= 120:
    print('você recebeu um doce!)
elif s >= 100:
    print('pão)
else:
nada de premio
'''

p = int(input()) 
d = int(input()) 
b = int(input())


s = p + (d * 2) + (b * 3)

if s >= 150:
    print('B')
elif s >= 120:
    print('D')
elif s >= 100:
    print('P')
else:
    print('N')

