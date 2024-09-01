c = 10

for p in range(0, 100):
    add = 0.33
    if p >= 25:
        add = 0.01
    if p >= 50:
        add = 0.001
    print(c)
    n = c * add
    c += n
