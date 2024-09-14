# desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla . No final, mostre: 
# quantas vezes aparece o valor 9
# em que posição foi digitada o primeiro valor 3
# Quais foram os numeros pares
lista = []
pares = []
num_nove = 0
posicao_3 = -1
# range ( 0 ,1 ,2 , 3, 4)
for i in range(4):
    valor = int(input(f"Digite o {i + 1} valor: "))
    lista.append(valor)
    # Quais foram os numeros pares
    if valor % 2 == 0:
        pares.append(valor)
    # quantas vezes aparece o valor 9
    if valor == 9:
        num_nove += 1
    # em que posição foi digitada o primeiro valor 3 (apenas na primeira vez que ocorre)
    if valor == 3 and posicao_3 == -1:
        posicao_3 = i
# conversão da lista em tupla
tupla = tuple(lista)
# impressão dos resultados
print(f" o valor 9 aparece: {num_nove} vezes")
print(f" os valores pares são {pares} ")
# previsão de erro na não ocorrência do numero 3
if posicao_3 != -1:
 print(f" o valor 3 apareceu na posição {posicao_3 + 1} ")
else:
   print(" o valor 3 não apareceu nenhuma vez")