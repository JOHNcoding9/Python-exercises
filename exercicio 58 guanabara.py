# melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10 só que agora o jogador irá tentar até acertar, mostrando ao final quantos palpites foram necessários para vencer
tentativas=0
import random
from time import sleep
print("tente advinhar o numero em que o computador está pensando")
print("computador pensando em um numero aleatorio ...")
sleep(6)
numero_computador=random.randint(0,10)
while True:
  print( '-'*30)
  print("Já pensei em um número, tente advinhar !")
  try:
   numero_jogador=int(input("escolha um numero entre 0 e 10: "))
   if numero_jogador==numero_computador:
    print(f"você VENCEU, o numero era {numero_computador}")
    break
   elif numero_jogador<0 or numero_jogador>10:
    print("o valor deve ser obrigatoriamente entre 0 e 10") 
   else:
    print("Menos que isso..." if numero_jogador>numero_computador else "Mais que isso ...")
    tentativas+=1
    print("<->" *30)
  except ValueError:
   print("Por favor , insira apenas números")
print("=" *30)
print("  FIM DE JOGO  ")
print("=" *30)
print(f"Acertou com {tentativas} tentativas, parabéns!")