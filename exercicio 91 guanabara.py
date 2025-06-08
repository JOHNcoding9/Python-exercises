# crie um jogo onde 4 jogadores joguem um dado e tenham resultados aleatórios . Guarde esses resultados em um dicionario . No final, coloque esse dicionario em ordem de vencedores


dicionario = {}
import random

for i in range(1,5):
    converter_para_string = str(i)
    dicionario["jogador_" + converter_para_string] = random.randint(1,6)

for chave,valor in dicionario.items():
    print(f"{chave} tirou {valor} no dado")

ordem_lugares = dict(sorted(dicionario.items(),key=lambda item: item[1], reverse=True))
print("=== Ranking dos jogadoes ===")

i = 1
for chave,valor in ordem_lugares.items():    
    print(f"{i}º lugar : {chave} com {valor} no dado")
    i += 1