#faça um programa ler três numeros e diga qual deles é o maior e menor deles:
lista=[]
for i in range(3):
 numero=float(input("digite um numero qualquer: "))
 lista.append(numero)
 print(f"valor {i+1}: " , numero)
print("o maior numero é: ", max(lista))
print("o menor numero é: ", min(lista))