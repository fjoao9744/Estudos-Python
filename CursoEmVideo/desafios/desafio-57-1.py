
sexo = str(input('digite seu sexo(M/F)')).upper().strip()
while sexo != "M" and sexo != 'F':
    print('valor invalido, tente novamente!')
    sexo = str(input('digite seu sexo(M/F)')).upper().strip()

print('sexo regristrado com sucesso')
