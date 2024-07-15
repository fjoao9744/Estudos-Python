
n1 = 0
n2 = 0
for c in range(1, 6):
    n = float(input('digite o peso da {}° pessoa'.format(c)))
    if c == 1:
        n2 = n


    if n >= n1:
        n1 = n
    if n <= n2:
        n2 = n

print('o maior peso foi de {} e o menor foi de {}'.format(n1, n2))



