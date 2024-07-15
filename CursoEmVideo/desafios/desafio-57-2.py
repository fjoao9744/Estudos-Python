sexo = str(input('digite seu sexo(M/F)')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('dados invalidos, digite seu sexo(M/F)')).upper().strip()[0]
print('sexo registrado com sucesso')

