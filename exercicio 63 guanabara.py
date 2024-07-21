# escreva um programa que leia um numero n  inteiro qualquer e mostre n primeiros numeros da seuqencia de fibonacci
print("====== Sequência de Fibonacci ============")
# criando lista para armazenar os termos de fibonacci
fibonacci=[0,1]
termos=int(input("Quantos termos da sequencia de fibonacci deseja mostrar? "))
# enquanto a quantidade de termos solicitado pelo usuario for maior do que o comprimento da lista:
while len(fibonacci)<termos:
    #adicionar a lista "fibonacci", a soma entre o valor na posição -1 da lista e o valor na posição -2 da lista
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(f" a sequencia de fibonacci com {termos} termos :")
print(fibonacci)