frase = 'Olá, Mundo! '

'''FATIAMENTO'''
print(frase[4])
print(frase[6:11])
print('{}\n '.format(frase[0:11:2]))

'''ANÁLISE'''

print(len(frase))
print(frase.count(' ', 0, 13))
print(frase.find('Mun'))
print('{}\n '.format('Mundo' in frase))

'''TRANSFORMAÇÕES'''

print(frase.replace('Mundo', 'World'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print('{}\n'.format(frase.strip())) 
'''rstrip ou lstrip'''

'''DIVISÃO'''
frase.split()
print('{}\n '.format(frase))

'''JUNÇÃO'''

print('{}\n'.format('-'.join(frase)))

''' EXTRAS'''
print("""a
a
a""") 

print(frase.lower().count('o'))
print(len(frase.strip().replace('Mundo!', 'ooooooooo')))
frase = frase.split()
print(frase[0] [0:3])
