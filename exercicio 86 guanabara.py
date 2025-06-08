# faça um programa que crie uma matriz de dimensão 3x3  . no final, mostre a matriz com a formatação correta

matriz = [ [0,0,0],[0,0,0],[0,0,0] ]
pares = soma = maximo = 0
maior = matriz[1][0]

for n in range(0,3): # posição na lista matriz
 for i in range(0,3): # posição da lista dentro da lista matriz
     matriz[n][i] = int(input(f"Digite o valor: { n , i } : "))
     if matriz[n][i] % 2 == 0:
       pares += matriz[n][i]

     soma += matriz[2][i]
     
     if matriz[1][i] > maior:
        maior = matriz[n][i]

print("=-="*40)

for p in matriz:
   for o in range(0,3):
    print("[",p[o],"]", end= " ")
   print()

print("=-="*40)

print("A soma dos valores pares é: ",pares)
print("A soma dos valores da terceira coluna é: ", soma)
print("O maior valor da segunda linha é: ", maior )