# Questão 1

def maximo(num1, num2):
    if(num1 > num2):
        print("O maior número é o primeiro número: ", num1)
    elif(num2 > num1):
        print("O maior número é o segundo número: ", num2)
    else:
        print("Os números são iguais: ", num1)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = maximo(num1, num2)
print(resultado)


