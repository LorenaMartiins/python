import os

def impar_par(num):
  if num%2 == 0:
    print("É PAR")
  else:
    print("É ÍMPAR")

x = int(input("Digite um número: "))

impar_par(x)

os.system("pause")