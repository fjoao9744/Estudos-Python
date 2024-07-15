nome = str(input('Digite uma frase: ')).strip().lower()
print('a letra A aparece {} na frase'.format(nome.count('a')))
print('a primeira letra a aparece na posição: {}'.format(nome.find('a')+1))
print('a ultima letra aparece na posição: {}'.format(nome.rfind('a')+1))