# crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. Ao final, mostre os valores pares e impares de forma crescente


numeros = [[],[]]

for i in range(7):
    number = int(input(f"Digite o numero {i + 1}: "))
    if number % 2 == 0:
        numeros[0].append(number)
    
    else:
        numeros[1].append(number)


print(f"Numeros pares: {sorted(numeros[0])}")
print(f"Numeros impares: {sorted(numeros[1])}")