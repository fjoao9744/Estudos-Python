from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')

print('''[0]pedra
[1]papel
[2]tesoura''')
op = int(input('qual a sua opção?' ))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

pc = randint(0, 2)

if (op == 0 and pc == 1) or (op == 1 and pc == 2) or (op == 2 and pc == 0):
    ganhador = '\033[0;31;40mvocê perdeu!\033[m'
elif (op == 0 and pc == 2) or (op == 1 and pc == 0) or (op == 2 and pc == 1):
    ganhador = '\033[0;32;40mvocê ganhou!\033[m'
elif op == pc:
    ganhador = '\033[0;37;40mdeu empate\033[m'
print('O computador jogou {} e você {}, {}'.format(itens[pc], itens[op], ganhador))


