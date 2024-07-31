lista = [[[]]]
from time import sleep
    

quant = 0
while True:
    lista[quant].append(str(input('Nome: ')).capitalize().strip())
    
    lista[quant][0].append(int(input('Nota 1: ')))
    lista[quant][0].append(int(input('Nota 2: ')))


    ver = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if ver == 'S':
        quant += 1
        lista.append([[]])
    else:
        break
 

print(f'No. NOME    MEDIA')
print('-' * 20)
for c, i in enumerate(lista):
    print(lista.index(i), end='  ')
    print(lista[c][1], end='    ')
    print((lista[c][0][0] + lista[c][0][1]) // 2)
while True:
    notas = int(input('Deseja mostrar as notas de qual aluno[999 para interromper]: '))
    if notas == 999:
        print('finalizando...')
        sleep(1)
        break

    print(f'a notas de {lista[notas][1]} são {lista[notas][0]}')
    
print('volte sempre.')



