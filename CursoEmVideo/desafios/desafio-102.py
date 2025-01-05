from time import sleep

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param num: numero que sera calculado o fatorial.
    :param show: (opcional) mostra o processo para alcançar o resultado.
    :result: retorna o valor calculado do fatorial.
    
    """
    aux = 1
    for c in range(1, num + 1):
        aux *= c
        if show:
            print(f'{c}', end=' x ', flush=True)
            sleep(0.3)
    if show:
        print("= ", end='')
            
    return aux
            
print(fatorial(5))
print(fatorial(5, show=True))
