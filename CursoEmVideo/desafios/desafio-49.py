n1 = int(input('digite um numero para ver sua tabuada '))
print('-'*20)
n2 = 0
for c in range(0, 10):
    n2 += 1
    print('{} x {} = {}' .format(n1, n2, n1*n2))

print('-'*20)