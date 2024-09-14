# faça o jogo par ou ìmpar com o computador e ao perder encerre o jogo e mostre a quantidade de vitòrias seguidas
import random
vitorias=0
# inicializando jogo
while True:
    #computador e jogador escolhem os valores
    computador = random.randint(0,10)
    jogador = int(input("Digite um numero: "))
    # escolha do jogador entre par ou ímpar
    while True:
     Par_ìmpar=str(input("Par ou Impar? ")).strip().lower()
     # validação da escolha
     if Par_ìmpar not in ["par","impar","ímpar"]:
        print("insira escolha válida")
     else:
        break
   # verificação dos resultados
    resultado = computador + jogador
    print(f"computador jogou {computador}, você jogou {jogador}, total: {resultado}")
    # condição de vitória ou derrota
    if (resultado%2==0 and Par_ìmpar!="par") or (resultado%2!=0 and Par_ìmpar not in ["impar","ímpar"]):
       print("você perdeu")
       break
    vitorias+=1
    print("ganhou essa rodada")
print(f"rodadas ganhas: {vitorias}")