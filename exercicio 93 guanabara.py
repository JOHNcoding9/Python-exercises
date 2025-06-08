# crie um programa que gerencie o aproveitamento de um jogador de futebol  e quantas partidas ewle jogou. Depois leia a quantidade de gols feitos ema cada partida . Guarde tudo em um dicionario, incluindo o total de gols durante o campeonato.
dicionario = {}
total_gols = 0


dicionario["nome"] = str(input("Nome jogador: "))
numero_partidas = int(input("Partidas realizadas: "))
gols = [0] * numero_partidas

for i in range(numero_partidas):
    gols[i] = int(input(f"Quantidade de gols na partida {i + 1}: "))
    total_gols += gols[i]
    dicionario['gols'] = gols
    dicionario['total_gols'] = total_gols
    

print("=-=" * 40)
print(dicionario)
print("=-=" * 40)

for chave,valor in dicionario.items():
    print(f"O campo {chave} tem o valor {valor}")
print("=-=" * 40)

print(f"O jogador {dicionario['nome'] } realizou {numero_partidas} partidas")
for partida,gol in enumerate(dicionario['gols']):
    print(f"==>  Na partida {partida + 1}º, fez {gol} gols")
print(f"foi um total de  {total_gols} gols")