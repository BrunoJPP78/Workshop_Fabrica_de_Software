print("*********************************")
print("Escolha a Atividade !!")
print("*********************************")

print("(1) Questão 1  |  (2) Questão 2 | (3) Questão 3")
exercicio = int(input("Digite um Número para selecionar a Questão: "))

if(exercicio == 1):
    print("--== Iniciando Questão 1 ==--")
    from Atividade1 import *

elif(exercicio == 2):
    print("--== Iniciando Questão 2 ==--")
    from Atividade2 import *

elif(exercicio == 3):
    print("--== Iniciando Questão 3 ==--")
    from Atividade3 import *
else:
    print("Você não escolheu nenhum exercício válido.")

