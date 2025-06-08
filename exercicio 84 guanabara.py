# faça um programa que leia o nome e peso de varias pessoas, guardando em uma lista. No final, mostre:
# quantas pessoas foram cadastradas
# uma lista com as pessoas mais pesadas
# uma lista com as pessoas mais leves 

leves = []
pesadas = []
cont = 0

while True:
    print("><" * 40)
    resposta = str(input("Deseja prosseguir? [S/N]   "))
    if resposta in "nN":
        print("saindo ...")
        break
    
    nome = str(input("Nome da pessoa: "))
    kilos_mortais = float(input("Peso do indivíduo: "))

    if cont == 0:
        maior = kilos_mortais
        menor = kilos_mortais
        pesadas.append(nome)
        leves.append(nome)

    else:
        if kilos_mortais > maior:
            maior = kilos_mortais
            pesadas = [nome] # Atualiza a lista de pesadas com a nova pessoa mais pesada
        elif kilos_mortais == maior:
            pesadas.append(nome)


        if kilos_mortais < menor:
            menor = kilos_mortais
            leves = [nome] # Atualiza a lista de leves com a nova pessoa mais leve
        elif kilos_mortais == menor:
            leves.append(nome)
    
    cont += 1

print(f"Você registrou {cont} pessoas .")
print(f"O maior peso foi de {maior} Kg ! {pesadas}")
print(f"O menor peso foi de {menor} Kg ! {leves}")