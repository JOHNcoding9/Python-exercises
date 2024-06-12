#faça um aplicativo que leia uma frase e mostre : a)Quantas vezes aparecem a letra A B)em que posição a letra A aparece pela primeira vez c) em que posição a letra A aparece pela ultima vez
frase=str(input("digite uma frase qualquer: ")).strip().upper()#.strip() remove todos os espaços adicionados na string e .upper() trnasforma a frase em maiusuclo
print("a letra  A aparece: ", frase.count("A"))#.count() conta a ocorrencia de vezes da letra A
print(" a letra A aparece pela primeira vez na poisção: ", frase.find("A")+1)#.find() encontra a poisção da letra A e adiicona +1 em seguida, ja que a contagem começa pelo 0
print(" a letra A aparece pela ultima  primeira vez na poisção: ", frase.rfind("A")+1)#.rfind() encontra a poisção da letra A começando  a partir do lado direito e adiicona +1 em seguida, ja que a contagem começa pelo 0
