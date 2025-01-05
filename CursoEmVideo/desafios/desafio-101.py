def voto(ano_nascimeto):
    if ano_nascimeto >= 18:
        return "VOTO OBRIGATÓRIO"
    if 16 <= ano_nascimeto < 18 or ano_nascimeto >= 65:
        return "VOTO OPCIONAL"
    if ano_nascimeto < 16:
        return "NÃO VOTA"
    
ano = int(input("Em que ano você nasceu? "))

idade = 2025 - ano

print(f"Com {idade} anos: {voto(ano)}")