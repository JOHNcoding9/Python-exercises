# leia o peso de 5 pessoas e mostre o menor e o maior peso
kg=[]
for i in range(5):
    peso=float(input(f"peso da pessoa {i+1}: "))
    kg.append(peso)
print(f" o maior peso é {max(kg)}")
print(f" o menor peso é {min(kg)}")

# ou
for i in range(5):
    peso=float(input(f"peso da pessoa {i+1}: "))
    if i==0:
        maior=peso
        menor=peso
    elif peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print(f" o maior peso é {maior}")
print(f" o menor peso é {menor}")