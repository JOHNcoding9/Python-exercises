# aprimore o deasfio 93 para que ele funcione com vários jogadores , incluindo um sistema de visualização de detalhes de  aproveitamento  de cada jogador


lista = []


while True:
 dicionario = {}
 total_gols = 0


 
 dicionario["nome"] = str(input("Nome jogador: "))
 numero_partidas = int(input("Partidas realizadas: "))
 dicionario['partidas_jogador'] = numero_partidas
 gols = [0] * numero_partidas

 lista.append(dicionario)

 for i in range(numero_partidas):
    gols[i] = int(input(f"Quantidade de gols na partida {i + 1}: "))
    total_gols += gols[i]
    dicionario['gols'] = gols
    dicionario['total_gols'] = total_gols
 while True:
  pergunta = str(input("Deseja continuar? [S/N] ")).upper()[0]
  if pergunta in "SN":
   break
 print("=" * 54)
 if pergunta == "N" :
    break
     

print("=-=" * 40)
print(lista)
print("=-=" * 40)
print("Lista de Jogadores:")
print("=-=" * 40)
print(f"{'CoD':<5} {'Nome':<15} {'Gols':<25} {'Total':<10}")
print("-" * 55)  # Linha de separação
for i in range(len(lista)):
    print(f"{i:<5} {lista[i]['nome']:<15} {lista[i]['gols']} {lista[i]['total_gols']:<10}")
print("=-=" * 40)

while True:
 pergunta = int(input("Mostrar dados de qual jogador? (999 para sair): "))
 if pergunta == 999:
   break
 print(f"-- LEVANTAMENTO DO JOGADOR {lista[pergunta]['nome']}")
 for i in range(lista[pergunta]['partidas_jogador']):
  print(f"==> Na partida {i + 1}, realizou {lista[pergunta]['gols'][i]} gols !")