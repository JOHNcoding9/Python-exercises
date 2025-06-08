# programa que leia nome, ano de nasciemnto, carteira de trabalho e cadastre-os com (idade) em um dicionario se por acaso os ctps forem diferentes de 0 , o dicionariio recebrá tambem o ano de contratação e o salário . Calcule a acrescente além da idade,  com quantos anos a pessoa irá se aposentar
from datetime import date
data_hoje = date.today().year

dicionario = {}

dicionario["nome"] = str(input("Nome: "))
dicionario["ano"] = int(input("Ano de nascimento: "))
dicionario["idade"] = data_hoje - dicionario["ano"]

carteira_trabalho = int(input("Cateira de trabalho ( não tem = 0 ): "))
if carteira_trabalho != 0:
 dicionario["carteira_trabalho"] = carteira_trabalho
 dicionario["ano_contatacao"] = int(input("Ano de contratação:  "))
 dicionario["aposentadoria"] = dicionario["idade"] + ((dicionario["ano_contatacao"] + 35) - data_hoje)
 dicionario["salario"] =  float(input("Salario:  "))

print("=-=-" * 40)
for chave , valor in dicionario.items():
 print(f"{chave} tem o valor {valor}")