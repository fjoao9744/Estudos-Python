def contador(inicio, fim, passo):
    """
    -> contador é uma função que serve para contar numeros
    :param inicio: qual numero vai começar a contagem
    :param fim: em qual numero vai acabar a contagem
    :param passo: de quanto em quanto que a contagem vai seguir
    :return: não retorna nada
        
    """
    for c in range(inicio, fim, passo):
        print(c)
    
    
contador(2, 10, 2)
help(contador)