#cire um programa que leia se um número é par ou ímpar
try:
 numero=int(input("Digite um numero inteiro: "))
except ValueError:
 print("!digite apenas numeros inteiros!")
try:
 if numero%2==0:
  print("este número é par")
 else:
  print("este numero é impar")
except NameError:
 print("!erro de cáculo de numero!")