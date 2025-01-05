from datetime import datetime

def voto(idade):
    if 18 <= idade < 65 :
        return "VOTO OBRIGATÓRIO"
    if 16 <= idade < 18 or idade >= 65:
        return "VOTO OPCIONAL"
    if idade < 16:
        return "NÃO VOTA"
    
ano = int(input("Em que ano você nasceu? "))

idade = datetime.now().year - ano

print(f"Com {idade} anos: {voto(idade)}")