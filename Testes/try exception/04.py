a = 5
b = 0

try:
    print(a/2) # nada é dividido por 0
    
except ZeroDivisionError as error:
    print(error)

else:
    print("se der certo, esse bloco vai rodar")

finally:
    print("esse bloco de comando vai acontecer se der erro e se não der")