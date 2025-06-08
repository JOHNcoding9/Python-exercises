from datetime import datetime

def voto(ano_nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    estado = 'VOTO OPCIONAL'

    if idade >= 18 and idade < 71:
        estado = 'VOTO OBRIGATÓRIO'
    
    if idade < 16:
        estado = "VOTO NEGADO"
    
    return estado, idade


    

ano_nasc = int(input("Em que ano você nasceu? "))
ano_idade = voto(ano_nasc)
print(f"Atualmente com {ano_idade[1]} anos ... {ano_idade[0]}")