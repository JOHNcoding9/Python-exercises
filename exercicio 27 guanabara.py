#faça um programa em pyhton que leia o nome completo de uma pessoa, mostrando em seguida seu primeiro e ultimo nome
nome=str(input("digite seu nome completo: ")).strip()
fatiado=nome.split()
print(fatiado)
print(f"seu primeiro nome é {fatiado[0]} e seu sobrenome é {fatiado[len(fatiado)-1]}")
