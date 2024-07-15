var2 = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        var2 += c

print('a soma de todos os valores solicitados é de {} e foram somados {} numeros'.format(var2, cont))
