def leiaDinheiro(text):
    while True:
        num = input(text).replace(",", ".")
        
        if num.isnumeric():
            break
        
        print(f"ERRO \"{num}\" é um preço invalido!")
        
    return int(num)
        
        