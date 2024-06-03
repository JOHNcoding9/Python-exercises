#faça um programa que leia o cateto oposto e o cateto adjacente e retorne o valor da hipotenusa 
import math
adjacente=float(input(' digite o valor do cateto adjacente: '))
oposto=float(input("digite o valor do cateto oposto: "))
hipotenusa= adjacente**2 + oposto**2
print("o valor da hipotenusa é de: ", math.sqrt(hipotenusa))
