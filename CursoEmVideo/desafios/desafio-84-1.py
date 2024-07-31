lista = []
pessoa = []

while True:
    pessoa.append(str(input('qual o seu nome? ').strip().capitalize()))
    pessoa.append(float(input('qual o seu peso? ')))
    lista.append(pessoa[:])
    pessoa.clear()

    if str(input('deseja continuar?[S/N] ').strip().upper()) == 'N':
        break