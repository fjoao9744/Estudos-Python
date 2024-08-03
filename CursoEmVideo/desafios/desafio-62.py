n1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
termos = 0
ultimo = 10
fim = False

while fim == False:
    while termos != ultimo:
        termos += 1
        print(n1, end=' ')
        form =  n1 + (ultimo-1) * r

        if n1 != form:
            n1 += r

        
    x = str(input('\ndeseja ver mais termos?[S/N] ')).strip().upper()
    if x == 'S':
        ultimo += int(input('quantos termos a mais deseja? '))
        
        
    else:
        fim = True
    
print(f'programa encerrado com {ultimo} termos')
    

    
