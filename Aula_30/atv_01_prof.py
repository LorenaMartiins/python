import os

print("------MENU------")
print("1 - Soma")
print("2 - Substração")
print("3 - Multiplicação")
print("4 - Divisão")
print("----------------------")
opc = int(input("Escolha a opção: "))
print("----------------------")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if opc == 1:
    print(n1,"+",n2,"=",n1+n2)
elif opc == 2:
    print(n1,"-",n2,"=",n1-n2)
elif opc == 3:
    print(n1,"x",n2,"=",n1*n2)
elif opc == 4:
    print(n1,"/",n2,"=",n1/n2)
else:
    print("Opção errada!")

os.system("pause")