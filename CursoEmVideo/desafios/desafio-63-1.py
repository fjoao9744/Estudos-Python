n1 = 0
n2 = 1

for c in range(0, 10):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n1, end=' ')

print('\n')

n1 = n2 = 1
for c in range(0, 5):
    print(n1, n2, end=' ')
    n1 = n1 + n2
    n2 = n2 + n1
    

