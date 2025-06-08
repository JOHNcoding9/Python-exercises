# faça um programa que tenham uma função chamada contador() que receba os parâmetros de início fim e passos . 
# o programa deve fazer três contagens : 
# de 1 até 10 de 1 em 1
# de 10 até 0 de 2 em 2
# uma contagem personalizada
from time import sleep

def contador(inicio,fim,passos):
    for i in range(inicio,fim + 1, passos):
     print(i)
     sleep(1)
    
contador(1,10,1)
print("=" * 45)
contador(10,0,-2)
print("=" * 45)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passos = int(input("Passos: "))
contador(inicio,fim,passos)


# Outro jeito
print("=" * 45)
def contador_2(inicio,fim,passos):
   if (inicio < fim and passos <= 0) or (inicio > fim and passos >= 0):
     print("Erro!") 
   else:
    while True:
     inicio = inicio + passos
     print(inicio)
     if inicio == fim:
       break
     sleep(1)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passos = int(input("Passos: "))
contador_2(inicio,fim,passos)