# crie um programa onde o usuario digite  uma expressão qualquer que tenha parênteses> Devverá analisar se a expressão é válida ou não


expressao = str(input("Digite sua expressão numérica: "))

pilha = []
for simbolo in expressao:
   
    if simbolo == '(':
        pilha.append('(')
        print(pilha)
   
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
            print(pilha)
        else:
            pilha.append(')')
            print(pilha)
            break

if len(pilha) == 0:
    print("expressão válida")
else:
      print("expressão não está válida")