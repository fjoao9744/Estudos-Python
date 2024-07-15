m1 = int(input('qual a idade da primeira irmã? '))
m2 = int(input('qual a idade da segunda irmã? '))
m3 = int(input('qual a idade da terceira irmã? '))



def media(a, b, c):
    if a <= b and a >= c or  a >= b and a <= c:
        return a == True
    

n = media(m1, m2, m3)
print(n)

