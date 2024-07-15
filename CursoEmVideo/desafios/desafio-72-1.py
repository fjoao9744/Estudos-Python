numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze','quatorze',
           'quinze', 'dezeseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')


while True:
    n = int(input('Digite um numero de 0 a 20: '))
    if 0 <= n <= 20:
        break

print(f'Você digitou o {numeros[n]}')