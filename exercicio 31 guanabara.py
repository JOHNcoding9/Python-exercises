#desenvolva um programa que pergunte a distãncia de uma viagem em km. Calcule o preço da passagem cobrando R$ 0.50 por km para viagens de até 200km e 0,45 para viagens mais longas
viagem=float(input("quantos Km você pretende viajar? "))
if viagem>200:
    print(f"você fará uma viagem de {viagem} km")
    print(f"será cobrado uma taxa de R$", viagem*0.45)
else:
    print(f"você fará uma viagem de {viagem} km")
    print(f"será cobrado uma taxa de R$", viagem*0.50)


    #outra maneira
viagem=float(input("quantos Km você pretende viajar? "))
preço= viagem*0.50 if viagem<=200 else viagem*0.45
print(f"você fará uma viagem de {viagem} km")
print(f"será cobrado uma taxa de R$", preço)