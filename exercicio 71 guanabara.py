# simulador de caixa eletrônico trabalhando com numeros inteiros e notas de 50, 20, 10 e 1
valor_sacado=int(input("Digite o valor a ser sacado: "))
notas_50 = valor_sacado // 50
resto_50 = valor_sacado % 50
notas_20 = resto_50 // 20
resto_20 = resto_50 % 20
notas_10 = resto_20 // 10
resto_10 = resto_20 % 10
notas_1 = resto_10 // 1
print(f"Total de notas de 50 : {notas_50}")
print(f"Total de notas de 20 : {notas_20}")
print(f"Total de notas de 10 : {notas_10}")
print(f"Total de notas de 1 : {notas_1}")


# outra maneira

total=int(input("valor a ser sacado: "))
for i in (50,20,10,1):
    total_cédulas=0
    while total>=i:
        total-=i
        total_cédulas+=1
    if total_cédulas!=0:
        print(f"total de cédulas de R$: {i} -> {total_cédulas}")