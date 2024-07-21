# leia o nome,idade e sexo de 4 pessoas e no final mostre:
# média de idade do grupo
# qual o nome do homem mais velho
# quantas mulheres têm menos de 20 anos
idadeS=[]
mais_velho=0
menor_que_20=0
for i in range(4):
    #lendo nome,idade e sexo de cada uma das 4 pessoas
    print(f" -------- {i+1}º PESSOA -------")
    nome=str(input("Digite seu nome: "))
    idade=int(input("Digite sua idade: "))
    while True: 
     sexo=str(input("Digite seu sexo: ")).upper()
     if not sexo in "FM":
        print("insira um sexo válido")
     else:
        break
    if sexo=="M" and idade>mais_velho:
       mais_velho = idade 
       nome_mais_velho = nome  
    if sexo=="F" and idade<20:  
       menor_que_20+=1
    idadeS.append(idade)
# média de idade do grupo
media=sum(idadeS)/len(idadeS)
print(f" a média de idade do grupo  é  {media:.2f} anos")
# nome do homem mais velho
print(f" o nome do homem mais velho é  {nome_mais_velho}, com {mais_velho} anos")

# quantas mulheres têm menos de 20 anos
print(f" Há {menor_que_20} mulheres com menos de 20 anos ")