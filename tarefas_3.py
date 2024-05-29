# Desenvolver um script em linguagem Python que leia a velocidade máxima permitida
#em uma avenida e a velocidade com que o motorista estava dirigindo por ela. Em seguida
#calcule o valor da multa que uma pessoa receberá, sabendo que são pagos: a) R$ 85,13 se
#o motorista ultrapassar em até 10 km/h a velocidade permitida; b) R$ 127,69 se o
#motorista ultrapassar de 11 a 30 km/h a velocidade permitida; c) R$ 574,62 se estiver
#acima de 31 km/h da velocidade permitida. Informe também os pontos que serão inseridos
#na carteira e o tipo de multa que será aplicado de acordo com a relação a seguir: Leve,
#Media e Gravíssima com 3, 5 e 7 pontos, respectivamente. Caso o motorista passe dentro
#da velocidade permitida, exibir “Vel. Normal”.
permitida = int(input(" velocidade permitida : "))
dirigida = int(input(" velocidade dirigida : "))
if dirigida>(permitida+31):
     print(f"voce andou {dirigida}km/h em uma rua de {permitida}GRAVE")
elif (permitida+11)<=dirigida<=(permitida+30):
 print(f"voce andou {dirigida}km/h em uma rua de {permitida} MEDIA")
elif dirigida==(permitida+10):
 print(f"voce andou {dirigida}km/h em uma rua de {permitida} LEVE")
else:
 print(f"velocidade normal")

#exercicio 2 Faça um script em linguagem Python que converta polegadas para milímetros;
polegada=float(input("insira o valor das polegadas "))
milimetro=25.4*polegada
print(f"{polegada} polegadas correspondem a {milimetro} mm ")
#exercicio 3 Criar um script em linguagem Python que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
#mês.
hora=int(input("quantas horas voce trabalha por mês ? "))
ganha=float(input("quantas voce ganha por hora trabalhada  ? "))
print(f"seu salario ao fim do mês será de {hora*ganha}")
#exercicio 4 João Pescador, homem de bem, comprou um microcomputador para controlar o
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
#estabelecido pelo regulamento de pesca do Estado (50 quilos) deve pagar uma multa de
#R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
#peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
#quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
#os dados do programa com as mensagens adequadas.
peixe=float(input("quantidade de kilos de peixe ? "))
excesso= peixe-50
if excesso>0 :
 print(f"você excedeu {excesso}kg do tolerável, recebrá uma multa de {4*excesso}")
else :
    print("quantidade dentro do limite")
#exercicio 5 Desenvolva um script em linguagem Python que pergunte quanto você ganha por hora
#e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
#mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
#5% para o sindicato, faça um programa que nos dê: salário bruto.
#• quanto pagou ao INSS.
#• quanto pagou ao sindicato.
#• o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
ganha=float(input("quanto ganha por hora? "))
hora=int(input("horas trabalhadas por mês? "))
salario=ganha*hora
imposto_renda=salario*0.11
inss=salario*0.08
sindicato=salario*0.05
print("salario bruto:", salario)
print("imposto de renda: ", imposto_renda)
print("valor inss: ", inss)
print("valor ao sindicato", sindicato)
print(f"salario líquido {salario-(imposto_renda+inss+sindicato)}")
   #exercicio 6 Faça um script em linguagem Python para a leitura de duas notas parciais de um
#aluno. O programa deve calcular a média alcançada por aluno e apresentar:
nota_1=float(input("nota 1 : " ))
nota_2=float(input("nota 2 : " ))
media=(nota_1+nota_2)/2
if media==10 :
 print("aprovado nerd")
elif media<7 :
 print("reprovado")
elif media>=7 :
 print("aprovado")
# exercicio 7 Elabore um script em linguagem Python que leia três números e mostre o maior e o menor deles
n_1=float(input(" nuemro 1 : "))
n_2=float(input(" nuemro 2 : "))
n_3=float(input(" nuemro 3 : "))
maior=n_1
if (n_2>maior)and (n_2>n_3):
 maior=n_2
elif(n_3>maior):
 maior=n_3
print("MAior", maior)
menor=n_1
if (n_2<menor) and (n_2<n_3):
 menor=n_2
elif(n_3<menor):
 menor=n_3
print("Menor", menor)
#exercicio 8 Desenvolva um script em linguagem Python que peça os 3 lados de um triângulo. O
#programa deverá informar se os valores podem formar um triângulo. Indique, caso os
#lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
lado_1=float(input(" lado1 : "))
lado_2=float(input(" lado 2 : "))
lado_3=float(input(" lado 3 : "))
if (lado_1+lado_2)>lado_3 :
 print("triãngulo válido")
 if (lado_1==lado_2) and (lado_2==lado_3):
  print("triangulo equilátero")
 elif (lado_1==lado_2) or (lado_2==lado_3) or (lado_3==lado_1) :
  print("traingulo isoceles")
 else:
     print("escaleno")
else:
    print("triangulo invalido")
#exercício 9 Fazer um script em linguagem Python que solicita um número decimal e imprime o
#correspondente em hexa, binário e octal.
a=int(input("número decimal "))
print(f"número {a} em octal : {oct(a)}")
print(f"número {a} em binário : {bin(a)}")
print(f" numero {a} em hexadecimal: {hex(a)}")
