def leia_int(msg):
     while True:
        entrada = input(msg).strip()  # Solicita a entrada do usuário
        if entrada.isdigit():  
            return int(entrada)  
        else:
            print("ERRO! Digite um número inteiro válido.") 

n = leia_int("Digite um numero: ")
print(f"você digitou o numero {n}")