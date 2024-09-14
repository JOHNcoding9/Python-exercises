# crie uma tupla com os 20 primeiros times na tabela do brasileirão e depois mostre:
# os 5 primeiros
# os 4 ultimos
# times em ordem alfabetica
# em que posição está a Cruzeiro

tabela_brasileirao = (
    "Botafogo", "Palmeiras", "Flamengo", "Grêmio", "Fluminense", 
    "São Paulo", "Bragantino", "Internacional", "Athletico-PR", 
    "Fortaleza", "Cruzeiro", "Atlético-MG", "Santos", "Bahia", 
    "Cuiabá", "Goiás", "Vasco", "Corinthians", "América-MG", 
    "Coritiba", "Chapecoense"
)

print(f"Os cinco primeiros colocados são: {tabela_brasileirao[:5]} ")
print('=' * 30)
print(f"Os quatro ultimos colocados são: {tabela_brasileirao[-4:]} ")
print('=' * 30)
print(f"Os times em ordem alfabética estão: {sorted(tabela_brasileirao)} ")
print('=' * 30)
print(f"Cruzeiro está na posição: {tabela_brasileirao.index('Cruzeiro') + 1}") 