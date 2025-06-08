# faça um programa que tenha uma função maior() que receba vários parâmetros com valores inteiros . seu valor deve analisar todos os valores e dizer qual deles é o maior
from time import sleep

def maior(valores):

    print('Analisando os valores informados ...')
    sleep(0.3) 


    informados = len(valores)

    if valores:
     maior = valores[0]

     for valor in valores:
       sleep(0.3) 
       print(valor, end= ' ', flush=True)

       if valor > maior:
          maior = valor

    else:
      maior = 'nada'

    print()
    mensagem_1 = print(f"Você informou {informados} valores e o maior numero entre eles foi {maior}")

    return mensagem_1
       

lista = [1,6,3,9,6,3,54,12,88,54,2,9]
maior(lista)
print("=" * 40)

lista = [5,6]
maior(lista)
print("=" * 40)

lista = [5]
maior(lista)
print("=" * 40)

lista = []
maior(lista)