#cire um programa que leia um número real qualquer pelo teclado e mostre na tela a porção inteira
import math
real=float(input("digite um número real: "))
print(f"sua porção inteira é {math.trunc(real)}")