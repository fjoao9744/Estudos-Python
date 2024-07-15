numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze','quatorze',
           'quinze', 'dezeseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero de 0 a 20: '))
    while n not in range(0, 20):
        n = int(input('valor informado invalido \nDigite um numero de 0 a 20: '))
    print(f'Você digitou o {numeros[n]}')
    cont = str(input('Você deseja continuar?[S/N] ')).strip().upper()
    del(n)
    if cont == 'N':
        break
print('fim do programa')


