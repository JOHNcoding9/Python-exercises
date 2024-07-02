#Crie um jogo de advinhação numérica com o computador
while True:
 import random
 from time import sleep
 vidas=3
 while vidas!=0:
  print("tente advinhar o numero em que o computador está pensando, numero de VIDAS =", vidas)
  print("computador pensando em um numero aleatorio ...")
  sleep(6)
  numero_computador=random.randint(0,5)
  print( '-'*30)
  print("Já pensei em um número, tente advinhar !")
  try:
   numero_jogador=int(input("escolha um numero entre 0 e 5: "))
   if numero_jogador==numero_computador:
    print(f"você VENCEU, o numero era {numero_computador}")
    break
   elif numero_jogador<0 or numero_jogador>5:
    print("o valor deve ser obrigatoriamente entre 0 e 5") 
   else:
    print(f'você PERDEU UMA VIDA, o numero era {numero_computador}')
    print("<->" *30)
    vidas-=1
  except ValueError:
   print("Por favor , insira apenas números")
 print("=" *30)
 print("  FIM DE JOGO  ")
 print("=" *30)
 break