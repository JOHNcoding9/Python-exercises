# leia o ano de nascimento de 7 pessoas , mostre quantas já atingiram a maioridade e quais ainda não 

from datetime import date
maioridade=0
menoridade=0
ano_atual=date.today().year
for i in range(7):
    idade=int(input(f"Em que ano a {i+1} pessoa nasceu? "))
    if ano_atual-idade>=18:
        maioridade+=1
    else:
        menoridade+=1
print(f" Dessas 7 pessoas, {maioridade} estão na maioridade")
print(f" Dessas 7 pessoas, {menoridade} são menores de idade")