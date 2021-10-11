import os

nome = input("Digite seu nome:")
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso/ (altura * altura)

print("NOME: ",nome, ", IMC:",imc)

os.system("pause")