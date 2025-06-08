# faça um programa que tenha uma lista chamada numeros e duas funções: sorteio() e Soma_pares( )
import random

numeros = [12,54,67,12,43,9,4,6,1,2,9,55,75,91,17,37,2,1,87,102,14,33,41,67,90,99,101]

def sorteios(valores):
   sorteio = random.sample(valores,5)
   return sorteio

def Soma_pares(valores):
    soma = 0
    for i in valores:
        if i % 2 == 0:
            soma+=i
            
    return soma

sorteio = sorteios(numeros)

print('Sorteando os 5 valores da lista: ', sorteios(sorteio))
print('Somando apenas os numeros pares:',Soma_pares(sorteio))