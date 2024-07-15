#1 1 2 3 5 8 13 21

n1 = n2 = 1
'''for c in range(0, 10):
    print(n1, n2, end=' ')
    n1 = n1 + n2
    n2 = n2 + n1'''
    
    
resp = int(input('quantos termos da sequencia de fibonacci você deseja ver? '))
ver = False

while ver == False:
    
    for c in range(0, resp - (resp // 2)):
        print(n1, n2, end=' ')
        n1 = n1 + n2
        n2 = n2 + n1
        
    ver1 = str(input('deseja continuar?[S/N] ')).strip().upper()
    if ver1 == 'S':
        resp = int(input('quantos termos você deseja ver agora? '))

    elif ver1 == 'N':
        ver = True
print('programa encerrado.')

