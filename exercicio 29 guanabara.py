#escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80 km mostre a mensagem de multa e aplique 7 reais por km acima do limite
velocidade=int(input("velocidade que o veículo está dirigindo na via: "))
km_acima_do_limite=velocidade-80
multa=km_acima_do_limite*7
if km_acima_do_limite>0:
    print(f"você ultrapassou os 80km permitidos da via por {km_acima_do_limite} km")
    print("recebrá uma multa de R$",multa)
else:
    print("velocidade dentro do limite")