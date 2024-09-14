# faça um programa para um loja
# leia o nome e o preço do produto
# pergunte se quer continuar
# exibir total gasto
# quantos produtos custam mais de 1000
# nome do produto mais barato
compras={}
cont=0
i=0
menor=None
mais_barato=None
total_gasto=0
while True:
    nome=str(input("nome do produto: "))
    preco=float(input("digite o preço do produto: "))
    if preco>1000:
        cont+=1
    i+=1
    compras[i] = {"nome":nome, "preco":preco}
    while (menor==None) or (compras[i]["preco"]<menor):
        menor = compras[i]["preco"]
        mais_barato = compras[i]["nome"]
    total_gasto+=preco
    pergunta=str(input("deseja continuar? [s/n] ")).strip().upper()
    if pergunta=="N":
        break
print(f"Total gasto: {total_gasto}")
print(f"Produtos acima de R$ 1000: {cont}")
print(f"Produto mais barato: {mais_barato}")