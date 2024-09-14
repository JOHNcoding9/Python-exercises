# crie um programa que vai criar vários numeros e coloca-lo dentro de uma lista. Depois disso, mostre
# quantos numeros foram digitados
# a lista de valores ordenada de forma decrescente
# se o valor 5 está ou não na lista
cinco_na_lista = False
lista = []

while True:
    valor = int(input("Digite um valor para adicionar a lista: "))
    
    lista.append(valor)
    
    resposta = str(input("Deseja continuar?  [Digite F para finalizar]: ")).strip()
    
    if resposta in'Ff':
        break
   
    if valor == 5:
        cinco_na_lista = True

print("><" * 40)
print(f"Valores digitados: {len(lista)}")
print("Numero 5 na lista: ", "verdadeiro" if cinco_na_lista else "Falso")
print(f"lista ordenada de forma decrescente: {sorted(lista,reverse = True)}")
