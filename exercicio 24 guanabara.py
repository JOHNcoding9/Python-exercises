#Crie um programa que leia o bnome de uma cidade e diga se começa com a palavra "Santo" em seu nome

cidade=str(input("nome da cidade: ")).strip() #usuário coloca o nome da cidade e o comando .strip() exclui qualquer espaço acidental do teclado
print(cidade[ :5].upper()=="SANTO") # com o cidade[ :5], verifica as 4 primeiras letras. em seguida, o comando .upper() deixa todas as 4 primeiras letras em maiúsuclo
#por fim, é verificado se após esse processo a palavra obtida é "SANTO"