def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    
    if idade < 16:
        return f"com {idade} anos: VOTO NEGADO"
    if 16 <= idade < 18 or idade > 65:
        return f"com {idade} anos: VOTO OPCIONAL "
    else:
        return f"com {idade} anos: VOTO OBRIGATORIO "

nasc = int(input("Em que ano você nasceu: "))
print(voto(nasc))