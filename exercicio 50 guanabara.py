# leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares 

soma=0
contador=0
#informando os 6 numeros 
for i in range(6):
    num=int(input(f"Digite o numero {i+1} : "))
    #aplicando a verfificação de numero par
    if num%2==0:
        # soma e contagem de numeros pares
        soma+=num
        contador+=1
print(f"você informou {contador} numeros pares e a soma deles deu: ",soma)