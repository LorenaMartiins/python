import os

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))

print("---------------------")
print("|         1         |")
print("|         2         |")
print("|         3         |")
print("|         4         |")
print("---------------------")
opcao = int(input("Escolha uma opção: "))
print("---------------------")

if opcao == 1:
    print("Multiplica os dois números!",n1,"*",n2,"=",n1*n2)
elif opcao == 2:
    print("Soma os dois números!",n1,"+",n2,"=",n1+n2)
elif opcao == 3:
    print("Divide!",n1,"/",n2,"=",n1/n2)
elif opcao == 4:
    print("Subtrai!",n1,"-",n2,"=",n1-n2)
else:
    print("Opção errada!")

os.system("pause")