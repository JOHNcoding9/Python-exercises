# faça um programa que leia vários numeros inteiros e informe a média entre todos os valores e qual foi o maior e menor numero lido sem o uso de listas
print("Digite ""Sair"" para sair")
quant = 0
Maior = None
Menor = None
num_total = 0

while True:
    num_adicionado = int(input("Digite um número qualquer: "))
    
    # Atualiza o maior e menor valor
    if Maior is None or num_adicionado > Maior:
        Maior = num_adicionado
    if Menor is None or num_adicionado < Menor:
        Menor = num_adicionado

    # Atualiza a quantidade e a soma dos números
    quant += 1
    num_total += num_adicionado
    
    pergunta = input("Deseja continuar? S/N ").strip().lower()
    if pergunta == "n":
        print("Saindo ...")
        break

# Calcula a média
media = num_total / quant

print(f"Você digitou {quant} números e a média entre eles foi: {media}")
print(f"O maior valor foi {Maior} e o menor foi {Menor}")
