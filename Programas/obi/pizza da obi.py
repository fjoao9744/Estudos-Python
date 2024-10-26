
n = int(input()) #numero de participantes
g = int(input()) #8 pedaços
m = int(input()) #6 pedaços

s = (g * 8) + (m * 6)

s1 = s


for c in range(s):
    n -= 1
    s1 -= 1

    if n == 0:
        break

print(s1)
