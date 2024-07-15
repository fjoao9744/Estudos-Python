tabela = ('smogon', 'capa', 'boa noite', 'grupo', 'mario', 'joao', 'game', 'free fire')


for palavra in tabela:
    print(f'\nna palavra {palavra.upper()} temos: ', end='')
    for letras in palavra:
        if letras in 'aeiou':
            print(letras, end=' ')
        

        
        