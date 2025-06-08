# leia o nome , sexo e idade de varias pessoas. Guarde os dados de cada pessoa em um dicionario e  todos os dicionariso em uma lista .Mostre:
# Quantas pessoas cadastradas
# A média da idade
# uma lista com mulheres
# lista com idade acima da média

quant = 0 
dicionario = {}
soma_idade = 0 
lista = []
mulheres = []


while True:
    sexo = " "
    pergunta = " " 
    quant += 1
    nome = str(input("Nome da pessoa: "))
    while sexo not in "MFmf":
     sexo = str(input("Sexo => [M/F]: "))
    idade = int(input("idade da pessoa: "))

    soma_idade += idade

    dicionario = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    }

    lista.append(dicionario)

    if sexo in "Ff":
      mulheres.append(dicionario)


    while pergunta not in "SN":
     pergunta = str(input("Vai continuar? [S/N] ")).upper()[0]
    if pergunta in "Nn":
      print("Encerrando ...") 
      break
    print("=" * 54)

print(lista)
media_idade = soma_idade / len(lista)

print("><" * 54)
print("A) Numero de pessoas cadastradas: ",quant)
print(f"B) Idade média das pessoas cadastradas: {media_idade:,.2f}")
print("C) Apenas mulheres cadastradas: ")
for i in range(len(mulheres)):
  print(mulheres[i]['nome'])

print("D) idades acima da média: ")
for i in range(len(lista)):
  if lista[i]['idade'] > media_idade:
    print(f"{lista[i]['nome']} com {lista[i]['idade']} anos")