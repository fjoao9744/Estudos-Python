#errado

lista = []
pessoa = []
pesos = []

while True:
    pessoa.append(str(input('qual o seu nome? ').strip().capitalize()))
    pessoa.append(float(input('qual o seu peso? ')))
    
    lista.append(pessoa[:])
    pessoa.clear()

    

    if str(input('deseja continuar?[S/N] ').strip().upper()) == 'N':
        break
    
for c in lista:
    pesos.append(c[1])
    
pesos.sort()
mais_pesado = pesos[-1]
mais_leve = pesos[0]
mais_leve1 = []
mais_pesado1 = []

for c in lista:
    if mais_pesado in c:
        mais_pesado1.append(c[0])
    if mais_leve in c:
        mais_leve1.append(c[0])

print(f'foram cadastradas {len(lista)} pessoas')
print(f'as pessoas mais pesadas foram: {mais_pesado1}')
print(f'as pessoas mais leves foram: {mais_leve1}')

    

        
