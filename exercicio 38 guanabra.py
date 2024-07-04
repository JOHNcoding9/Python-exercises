#escreva um programa que leia 2 numeros inteiros e compare os dois, exibindo qual é o maior pu se são iguais
numero_1=float(input("Digite o valor qualuer: "))
maior=numero_1
numero_2=float(input("Digite o valor qualuer: "))
if numero_2>maior:
    maior=numero_2
elif numero_2==maior:
    print("os dois Numeros são iguais")
print(f"o maior numero é: {maior}")