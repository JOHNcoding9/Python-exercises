#crie um programa que leia o nome de uma pessoa e mostre:
#o nome com todas as letras maiúsculas e minúsculas
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

nome=str(input("digite seu primeiro nome: ").strip()) # o comando .strip() irá remover os espaços no inico e fim da string
sobre=str(input("digite se sobrenome: ").strip())
nome_completo=nome+sobre #concatenar as duas strings em uma para a contagem total
print(nome.upper()+' '+ sobre.upper()) #comando .upper() deixa as letras MAIUSCULAS
print(nome.lower()+' '+ sobre.lower()) #comando .lower() deixa as letras minusculas
print(f"seu nome completo tem {len(nome_completo)- nome_completo.count(' ')} letras") # comando len() confere o tamanho da string, enquanto que count() faz a contagem de algo específico. Nesse caso, irá contar os espaços presentes entre o nome e o sobrenome da pessoa
print(f"seu primeiro nome tem {len(nome)- nome.count(' ')} letras")