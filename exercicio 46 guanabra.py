# fazer a contagem regressiva de uma explosão de fogos de artifício utilizando python indo de 10 até 0 com uma pausa de 1 segundo

from time import sleep
# definindo o numero inicial, o numero final (não incluso) e seguindo a razão -1 ( contagem regressiva)
for i in range(10,0,-1):
    print(i)
    sleep(1)
    if i==1:
        print("BUUUUUM!!!!!!")