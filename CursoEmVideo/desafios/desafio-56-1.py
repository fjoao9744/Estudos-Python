idadeH = 0
MIhomem = ''
idadeM20 = 0
media = 0

for c in range(1,5):
    print('---- {}ª pessoa ----'.format(c))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]:')).upper().strip()
    
    media += idade

    if c == 4:
        media //= 4

    if sexo == 'M' and idade > idadeH:
        idadeH = idade
        MIhomem = nome

    if sexo == 'F' and idade < 20:
        idadeM20 += 1



print('a media de idade entre as pessoas é de {}'.format(media))
print('o homem mais velho é o {} com {} anos'.format(MIhomem, idadeH))
print('tem  {} mulheres com menos de 20 anos'.format(idadeM20))