# crie um programa que leia dois valores e mostre um menu  de operações matemáticas
lista_numeros=[]
resultado=0
multiplicador=1
numero_1=float(input("Digite o numero a ser adicionado: "))
numero_2=float(input("Digite o numero a ser adicionado: "))
lista_numeros.append(numero_1)
lista_numeros.append(numero_2)
while True:
 print(""" MENU DE OPERAÇÕES
      Digite [0] para DIVIDIR
      Digite [1] para SOMAR
      Digite [2] para MULTIPLICAR
      Digite [3] para ver o MAIOR NUMERO
      Digite [4] para ADICIONAR NUMEROS
      Digite [5] para SAIR""")
# validar opções
 while True:
  opcao=int(input("Insira uma opção válida: "))
  if 0<=opcao<=6:
   break
# sair
 if opcao==5:
  print("saindo ...")
  break
 # dividir numeros
 if opcao==0:
    resultado=lista_numeros[0]
    for i in lista_numeros[1:]:
      resultado/=i
    print(f"A divisão  dos numeros {lista_numeros} deu : {resultado}")
# adicionar numeros
 if opcao==4:
  numero=float(input("Digite o numero a ser adicionado: "))
  lista_numeros.append(numero)
# somar
 if opcao==1:
  print(f"A soma dos numeros {lista_numeros} deu : {sum(lista_numeros)}")
# multiplicar
 if opcao==2:
  for numero in lista_numeros:
   multiplicador*=numero
  print(f"A multiplicação  dos numeros {lista_numeros} deu : {multiplicador}")
# ver maior numero
 if opcao==3:
  print(f"O maior numero é: {max(lista_numeros)}")