import requests

try:
    site = requests.get(r"https://pudim.com.br")
    print("O site do pudim esta no ar!")
    
except:
    print("O site do pudim NÃO esta no ar!")
