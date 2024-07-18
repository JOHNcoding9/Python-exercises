# um programa que calcule a soma de todos os numeros ìmpares que são multiplos de 3 e que se encontram no intervalo de  1 a 500

soma=[]
# definindo o numero inicial em 1, o final em 501 (não incluso) e a razão de 2 em 2
for i in range(1,501,2):
    if i%3==0:
        soma.append(i)
# soma dos i presentes na lista soma ( soma de todos os numeros que obedecem os critérios)
print("a soma de todos os numeros ìmpares que são multiplos de 3 e que se encontram no intervalo de  1 a 500: ", sum(soma))
# lista dos numeros que obedecem os critérios
print(soma)