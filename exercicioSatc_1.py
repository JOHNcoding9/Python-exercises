# Crie uma função que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os números pares

def pares(lista):
    lista_2 = []
    for numero in lista:
     if numero % 2 == 0:
        lista_2.append(numero)
    return lista_2
lista = [1,2,3,4,5,6,7,8,9,10]
print(f"numeros pares da lista : {pares(lista)}")


# Outra Maneira de fazer masi simplificada :

def pares(lista):
    return [numero for numero in lista if numero % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"números pares da lista: {pares(lista)}")
