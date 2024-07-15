n1 = n2 = 0
ver = False
while ver == False:
    n1 = int(input('digite um numero'))
    if n1 < 999:
        n2 += n1
    elif n1 >= 999:
        ver = True

print('a soma dos valores digitados foi de {}'.format(n2))

