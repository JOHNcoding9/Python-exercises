# Crie uma função que recebe uma lista vazia e permite ao usuário adicionar 5 elementos a essa lista. Ao final, a função deve retornar a lista completa.

lista = []

def adicionar_lista(lista):
    for i in range(5):
        numero = input(f"adicione o {i+1} elemento da lista: ")
        lista.append(numero)
    return lista
print(" lista completa: ", adicionar_lista(lista))


#  outra maneira mais simplificada
def adicionar_lista():
    # List comprehension para criar a lista de forma mais concisa
    return [input(f"adicione o {i+1} elemento da lista: ") for i in range(5)]

# Chamada da função e impressão do resultado
print("Lista completa:", adicionar_lista())
