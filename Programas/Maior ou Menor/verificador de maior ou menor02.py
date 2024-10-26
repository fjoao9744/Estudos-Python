#criando variaveis iniciais
menor = maior = numero = 0 
continuar = ''

#o fim vai ser a condição de parada
fim = False

while fim == False:
    #criando o numero que vai ser verificado
    numero_antigo = numero
    
    #pergunta o numero
    numero = int(input('Digite um numero: '))
    #verificando
    if numero >= numero_antigo:
        maior = numero
        menor = numero_antigo
    if numero <= numero_antigo:
        maior = numero_antigo
        menor = numero

    #deseja continuar?
    continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()

    #verificando a condição de parada
    if continuar == 'N':
        fim = True

print('O menor numero foi {} e o maior foi {}'.format(menor, maior))