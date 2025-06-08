# faça um programa que ajude um jogador da MEGA SENA  a criar palpites . O programa irá perguntar quantos jogos serão gerados  e vai sortear 6 numeros entre 1 e 60  para cada jogo. Cadastrando tudo em uma lista completa
# os numeros não podem se repetir dentro da lista

import random
from time import sleep

lista = []

print("><" * 12)
print("    Jogo da Mega Sena    ")
print("><" * 12)

jogos = int(input("Quantos jogos serão feitos? "))

print("-=-" * 12 )
print(f"SORTEANDO OS {jogos} JOGOS")
print("-=-" * 12 )

for i in range(jogos):
    sleep(2.2)
    while len(lista) < 6:
        
        sorteio = random.randint(1,60)
        
        while sorteio in lista :
            sorteio = random.randint(1,60) 
    
        lista.append(sorteio)
 
    print(f"jogo {i + 1} : {lista}")
    lista = []

print("><" * 6 , "BOA SORTE","><" * 6)