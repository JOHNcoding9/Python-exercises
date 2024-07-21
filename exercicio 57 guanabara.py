# faça um programa que pergunte o sexo do usuário mas só aceite M ou F como resposta
while True: 
     sexo=str(input("Digite seu sexo: ")).strip().upper()
     if sexo not in ["M", "F", "MASCULINO", "FEMININO"]:
        print("insira um sexo válido")
     else:
        break
print(f"Verificação concluìda, usuário de sexo {sexo}")