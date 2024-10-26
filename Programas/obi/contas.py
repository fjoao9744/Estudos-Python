''' aluguel, conta de luz, conta de água, telefone celular, conta do mercado'''
#açougue, farmacia e padaria
v = int(input()) #disponivel
a = int(input()) 
f = int(input())
p = int(input())

s = v

if v < a or v < f or v < p:
    print(0)
else:
    if (s - a) > 0:
        s -= a
    
        if (s - f) < 0 and (s - p) < 0:
            print(1)
        
        else:
            if (s - f) > 0:
                s -= f
                if (s - p) < 0 :
                    print(2)
            if (s - p) > 0:
                s -= p
                if (s - f) < 0 :
                    print(2)
            else:
                print(3)
    else:
        print(0)

