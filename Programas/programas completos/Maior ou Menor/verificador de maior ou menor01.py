#qual vai ser o menor e o maior numero
menor = 0 
maior = 0

#perguntando os numeros
numero = int(input('Digite um numero: '))
numero1 = int(input('Digite outro numero: '))

#verificando
if numero >= numero1:
    maior = numero
    menor = numero1
if numero <= numero1:
    maior = numero1
    menor = numero

#mostrando
print('o menor numero foi {} e o maior foi {}'.format(menor, maior))


