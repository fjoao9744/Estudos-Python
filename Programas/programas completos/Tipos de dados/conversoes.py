'''
str
int
float
bool
complex
list
tuple
set
dict

'''
dado = input('digite algo para fazermos as conversões dos tipos de dados: ').strip() #pega o valor

#string
print(f'seu valor como string: "{str(dado)}"') 

#inteiro
try:
    print(f'seu valor como inteiro: {int(dado)}') 
except:
    print(f'seu valor não pode ser um inteiro')

#flutuante
try:
    print(f'seu valor como flutuante: {float(dado)}')
except:
    print(f'seu valor não pode ser um flutuante')

#booleano
if dado in '01':
    print(f'seu valor como booleano: {(bool(int(dado)))}')
elif dado == 'True' or dado == 'False':
    print(f'seu valor como booleano: {dado == 'True'}')
else:
    print(f'seu valor não pode ser booleano')


dado = list(dado[:])
while ' ' in dado:
    dado.remove(' ')
while ',' in dado:
    dado.remove(',')
#tupla

print(f'seu valor como tupla: {tuple(dado)}')

#lista
print(f'seu valor como lista: {dado}')

#conjunto
print(f'seu valor como conjunto: {set(dado)}')


