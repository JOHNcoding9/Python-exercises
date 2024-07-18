# mostre a tabuada de um numero que o usuário escolher utilizando laço for

tabuada=int(input("Escolha a tabuada que deseja: "))
# definindo o inicio da range em 1 e o fim em 11 (não incluso)
for i in range(1,11):
    print(f"{tabuada} x {i} = {tabuada*i}")