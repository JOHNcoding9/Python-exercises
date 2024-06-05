import math
# exercicio 1 (faça um programa que defina a distância entre dois pontos em um plano cartesiano)
x_1 = int(input("defina a coordenada x1 do poonto 1 : "))
y_1 = int(input("defina a coordenada y1 do poonto 1 : "))
x_2 = int(input("defina a coordenada x2 do poonto 2 : "))
y_2 = int(input("defina a coordenada y2 do poonto 2 : "))
dist = ( x_2 - x_1 )**2 + (y_2 - y_1)**2
print( " a distancia entre os dois pontos é de : " , dist)

#exercico 2 (Uma imobiliária paga aos seus corretores um salário base de R$
#1.500,00. Além disso, uma comissão de R$ 200,00 por cada imóvel
#vendido e 5% do valor de cada venda. Construa um programa que
#solicite o nome do corretor, a quantidade de imóveis vendidos e o valor
#total de suas vendas. Ao fim, o programa deve calcular e escrever o
#salário final do corretor de imóveis.)
nome = input(" qual o seu primeiro nome ? " )
sobrenome = input("qual o seu sobrenome? " )
imovel = int(input("qual a quantidade de imoveis vendidos? "))
valor_venda = float(input("qual o valor da venda total ? " ))
salario = 1500 + (200*imovel) + (0.05*valor_venda)
print ( nome + " " + sobrenome )
print(" valor de seu salário: " , salario , "reais")

#EXERCICIO 3 (Elabore um código fonte que calcule a hipotenusa de um triângulo
#retângulo, cujos catetos serão fornecidos pelo usuário.)
cateto_1 = float(input("insira um dos catetos" ))
cateto_2 = float(input("insira um dos catetos" ))
x = (cateto_1**2 ) + (cateto_2**2)
print(" o valor da hipotenusa é " , math.sqrt(x))

#exercicio 4 Desenvolva um script que solicite dois números quaisquer e mostre o maior entre
#eles.

x = float(input(" digite um numero qualquer "))
y = float(input(" digite um numero qualquer "))
maior=x
menor=y
if (y>maior):
    maior=y
    menor=x
print(maior, " é maior do que ", menor)

#exercicio 5 Elabore um programa que verifique se uma letra digitada é "F" ou "M". Conforme a
#letra escrever: F - Feminino, M – Masculino ou Sexo Inválido.
sexo = input("qual seria o seu gênero? ")
if sexo in ["F", "f"] :
    print("feminino")
elif sexo in ["M", "m"] :
 print("masculino")
else :
    print("sexo invàlido")

#exercicio 6 Escreva um programa que verifique se uma letra digitada é vogal ou consoante. Ou
#ainda se não está nestes grupos.
letra = input("digite uma letra ")
if not letra.isalpha() :
    print("não pertence ao alfabeto")
elif letra in ["A", "a", "E", "e", "i" , "I", "O", "o", "U", "u"] :
 print("essa letra é uma vogal")
else:
    print(" a letra é uma consoante")
 #exercicio 7 Crie um programa em Python para calcular a média de três notas inseridas pelo
#usuário e dar feedback baseado na média calculada.
#Peça ao usuário para inserir as notas de três avaliações.
#Calcule a média das notas e arredonde-a para duas casas decimais.
#Exiba a média na tela.
#Dê um dos seguintes feedbacks de acordo com a média:
#Média maior ou igual a 7.0: "Parabéns! Sua média é alta."
#Média maior ou igual a 5.0: "Sua média é razoável."
#Média abaixo de 5.0: "Sua média é baixa. É uma boa oportunidade para melhorar.".
nota_1 = float(input("insira a primeira nota : "))
nota_2 = float(input("insira a segunda nota : "))
nota_3 = float(input("insira a terceira nota : "))
media = (nota_1 + nota_2 + nota_3 ) / 3
x = round(media,2)
if media>7 :
    print(f"parabens, você é anormal e conseguiu acima da média {x}")
elif 5<media==7 :
    print(f"nota razoavel, jogou muito valorant de novo? {x}")
else:
    print(f"conseguiu ascendente pelo menos? {x} ")
#exercicio 8 (  realize uma troca de valores com uma variável auxiliar)
a=input("variável a ")
b=input("variável b ")
c=a
a=b
b=c
print(a, "valor de a ")
print(b, "valor de b ")
#exercicio 9 ( diga se um ano é bissexto. um ano é bissexto quando é divisível por 400 ou divisivel 4 e não divisível por 100)
ano=int(input("insira um ano "))
if math.fmod(ano,400)==0 :
    print("ano bissexto")
elif math.fmod(ano,4)==0 and math.fmod(ano,100)!=0:
 print("ano bissexto")
else:
    print("ano normal")
    



    


                    
                    
             
