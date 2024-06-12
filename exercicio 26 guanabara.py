frase=str(input("digite uma frase qualquer: ")).strip().upper()
print("a letra  A aparece: ", frase.count("A"))
print(" a letra A aparece pela primeira vez na poisção: ", frase.find("A")+1)
print(" a letra A aparece pela ultima  primeira vez na poisção: ", frase.rfind("A")+1)