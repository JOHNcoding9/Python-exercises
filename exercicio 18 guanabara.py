# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo=float(input("digite um angulo auqluer: "))
print(f""" o valor do coseno é de {math.cos(math.radians(angulo))}
o valor do seno é de {math.sin(math.radians(angulo))}
o valor da tangente é de {math.tan(math.radians(angulo))}""")
