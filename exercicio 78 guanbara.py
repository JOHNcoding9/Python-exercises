# faça um programa que leia 5 valores numericos  e guarde os em uma lista. No final, mostre o maior e o menor valor e suas posições
numeros = []
for i in range(5):
    numeros.append(int(input(f"Digite o valor da posição {i + 1}: ")))
    if i == 0:
        maior =  numeros[i]
        menor = maior
    else:
        if numeros[i] > maior:
            maior =  numeros[i]
        if numeros[i] < menor:
            menor =  numeros[i]

print("Você digitou: ", numeros)
print("Maior valor: ",maior)
print("Posições: ")
for i,v in enumerate(numeros):
    if numeros[i] == maior:
     print(f"{i} ... ", end="")
print("=-=" * 40)
print("Menor valor: ",menor)
print("Posições: ")
for i,v in enumerate(numeros):
    if numeros[i] == menor:
     print(f"{i}... ", end="")