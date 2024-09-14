# crie um programa que vai ler varios numeros e colocar em uma lista. Em seguida, crie duas listas extras que vão conter apenas os valores pares e os valores impares . Ao final, mostre o conteudo das três listas geradas

todos = []
pares = []
impares = []

while True:
    resposta = str(input("Deseja continuar?  [Digite F para finalizar]: ")).strip()
    
    if resposta in'Ff':
        break

    valor = int(input("Digite um valor para adicionar a lista: "))
    
    todos.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
        
    else:
        impares.append(valor)
print("><" * 40)
print(f"Todos os numeros digitados: {todos}")
print(f"Todos os numeros pares digitados: {pares}")
print(f"Todos os numeros impares digitados: {impares}")