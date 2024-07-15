n1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
termos = 0
form =  n1 + (10-1) * r

while termos != 10:
    termos += 1
    print(n1, end=' ')
    
    if n1 != form:
        n1 += r
    
