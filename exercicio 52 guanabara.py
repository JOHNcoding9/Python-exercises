# faça um programa que leia um numero inteiro e diga se ele é ou não primo

numero=int(input("Digite um numero: "))
contador=0
for a in (1,2,3,4,5,6,7,8,9):
 if numero%a==0:
  contador+=1
  print(f"\033[0;33m{a}\033[m",end=" ")
 else:
  print(a, end=" ")
print(" ")
print(f"O numero {numero} foi divisivel {contador} vez(es) (além dele mesmo)")
if contador>2:
 print("NÃO É um numero primo")
else:
  print("É um numero primo")