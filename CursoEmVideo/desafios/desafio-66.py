s = n = c = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    c += 1
    s += n

print(f'foram digitados {c} valores e sua soma é de {s}')
