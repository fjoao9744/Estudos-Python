var2 = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        var2 = var2 + c
        print(c)

print(var2)
