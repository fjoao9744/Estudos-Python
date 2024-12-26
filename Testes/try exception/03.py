a = 5
b = 0

try:
    print(a/b) # nada é dividido por 0
    
except ZeroDivisionError as error:
    print(error)
    
finally:
    print("esse bloco de comando vai acontecer se der erro e se não der")
