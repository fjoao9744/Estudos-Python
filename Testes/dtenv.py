from dotenv import load_dotenv
import os

load_dotenv() # carrega as variaveis

teste = os.getenv("TESTE") 

print(teste) # printando uma variavel privada