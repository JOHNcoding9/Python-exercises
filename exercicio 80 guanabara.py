# faça um programa em que o usuario digite 5 valores numericos  e cadastre-os em uma lista , já na posição correta sem usar o sort() . Ao final, mostre a lista ordenada na tela

valores = [""] * 5


# iteração  de cada posição de 0 a 5
for posicao_atual in range(5):
    valor = int(input(f"Digite o valor {posicao_atual + 1} : "))

    # definindo o primeiro numero digitado pelo usuario como parâmetro para os demais
    if posicao_atual == 0:
        valores[0] = valor
       
   
    else:
        # descobrir posição do novo elemento digitado pelo usuario
        posicao_elemento = 0
        for j in range(posicao_atual): # O loop for j in range(i) garante que só comparamos até o índice atual j =intervalo entre
          
          # Achar posição do novo elemento
         if valores[j] > valor:
            posicao_elemento = j
            break
         else: # valores[j] < valor:
            posicao_elemento += 1

        # realocar as posisções
        for x in range(posicao_atual, posicao_elemento, -1):
           valores[x] = valores[x - 1]
        
        # atribuição do valor digitado pelo usuário a posição designada
        valores[posicao_elemento] = valor
      

print(valores)