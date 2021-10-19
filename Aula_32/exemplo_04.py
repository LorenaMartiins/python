import os

def soma(n1, n2):
    print(n1,"+",n2,"=",n1+n2)
def sub(n1, n2):
    print(n1,"-",n2,"=",n1-n2)
def mult(n1, n2):
    print(n1,"x",n2,"=",n1*n2)
def div(n1, n2):
    print(n1,"/",n2,"=",n1/n2)

print("---------------------")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
print("---------------------")
opc = int(input("Digite a opção:"))

if opc >= 1 and opc <= 4:
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite outro número:"))
print("---------------------")

if opc == 1:
    soma(n1, n2)
elif opc == 2:
    sub(n1, n2)
elif opc == 3:
    mult(n1, n2)
elif opc == 4:
    div(n1, n2)
else:
    print("Erro na opção!")
  
print("---------------------")

os.system("pause")