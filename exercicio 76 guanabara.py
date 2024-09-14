# crie um programa que tenha uma tupla unica  com o nome dos produtos e seus preços, na sequencia . no final, mostre a listagem de preços organizados de forma tabular

produtos = (
    "Arroz", 15.90,
    "Feijão", 7.50,
    "Macarrão", 4.30,
    "Leite", 3.80,
    "Carne", 29.90,
    "Açúcar", 2.50,
    "Óleo", 5.99,
    "Café", 8.75
)

# Exibindo a listagem de preços de forma tabular
print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)

for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]
    print(f"{produto:<30} R$ {preco:>7.2f}")

print("-" * 40)