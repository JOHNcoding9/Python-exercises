#crie um script que faça o computador jogar JOKENPO com você
import random
from time import sleep
escolhas=("Pedra","Papel","Tesoura")
computador=random.choice(escolhas)
print("Jogue Pedra, papel e Tesoura com o Computador!")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")
while True:
 jogador=int(input("Digite aqui sua escolha: "))
 if 0<=jogador<=2:
  break
jogada=escolhas[jogador]
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1.5)
print("PO")
print("-=-"*30)
print(f"Computador jogou {computador}")
print(f"Jogador jogou {jogada}")
print("-=-"*30)
if jogada==computador:
 print("EMPATE !!")
elif jogada=="Pedra" and computador=="Papel" or jogada=="Papel" and computador=="Tesoura" or jogada=="Tesoura" and computador=="Pedra":
 print("Você Perdeu !!")
else:
 print("Você Venceu !!")
