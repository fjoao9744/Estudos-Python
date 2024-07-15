nome = str(input('digite seu nome completo: ')).strip()
n1 = nome.lower()
n2 = nome.upper()
n3 = len(nome) - nome.count(' ')
n4 = nome.split()

print('Em minusculo: {} \nEm maiusculo: {} \nQuantas letras tem: {} \ne seu primeiro nome é: {}, e tem {} letras'.format(n1, n2, n3, n4[0], len(n4[0]) ))
