#Desisto

primeiro_termo = int(input('qual o primeiro termo da P.A: '))
razão = int(input('qual a razão da P.A: '))
termos = 0
quantidade = 10
ultimo_termo = primeiro_termo + (quantidade-1) * razão 
mais = 10
while quantidade != 0:
    while primeiro_termo != ultimo_termo + razão:
        print(primeiro_termo, end=' ')
        primeiro_termo += razão
        termos += 1
    
    quantidade = int(input('\nquantos termos a mais você deseja mostrar: ')) 
    ultimo_termo = primeiro_termo + (quantidade-1) * razão 
    
print(f'programa encerrado com {termos} termos')
