
#cire um programa que leua o nome de uma pessoa e diga se seu nome possui "Silva"

nome=str(input("digite seu nome: ")).strip() # .strip() corrige qualquer espaço digitado acidentalemnte
print("Seu nome tem silva?", "SILVA" in nome.upper())
#"SILVA" in nome.upper() verifica se após eu deixar o nome da pessoa em maiúsuclo, eu obtenho a palavra "SILVA" dentro do nome desa pessoa
#o valor retornado deve ser booleano
