n1 = int(input('qual numero você deseja ver o fatorial: '))
count, n2 = n1, 1

while count > 0:
    print(f'{count}',  'x' if count > 1 else f'= {n2}', end=' ')
    n2 *= count
    count -= 1

