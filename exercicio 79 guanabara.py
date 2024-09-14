# Crie um programa onde o usuario possa digitar varios valores e cadastre-os em uma lista, caso o numero já exista ele não será adicionado. No final, serão exibidos todos os valores unicos da lista em ordem crescente

eliminar_duplicatas = set()

vezes = int(input("Quantidade de numeros a serem digitados: "))

for i in range(vezes):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    eliminar_duplicatas.add(valor)

lista = sorted(eliminar_duplicatas)
print(f"Valores em ordem crescente : {lista}")