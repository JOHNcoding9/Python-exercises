 # crie um programa que irá gerar 5 numeros aleatorios e colocará eles em uma tupla, depois disso, msotre a listagem de numeros , o maior e o menor
import random
tupla = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
print('lista de numeros: ', tupla)
print(" maior numero : ", max(tupla))
print(" menor numero : ", min(tupla))