import os

r = "s"

while r == "s" or r == "S":
    #Limpa a tela do prompt de comandos
    os.system("cls")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    print("---------------------")
    print(n1,"+",n2,"=",n1*n2)
    print("---------------------")
    r = input("Deseja continuar? (S/N) \n")

os.system("pause")