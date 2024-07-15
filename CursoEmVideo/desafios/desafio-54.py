n1 = 0
n2 = 0

for c in range(1, 8):
    n = int(input('digite o ano que a {}° pessoa nasceu: '.format(c)))

    if n >= 2000:
        n1 += 1

    else:
        n2 += 1

print('ao todo tivemos {} pessoas de maior idade e {} pessoas de menor idade'.format(n2, n1))