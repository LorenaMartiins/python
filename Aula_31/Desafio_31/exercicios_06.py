# Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.

import os

n = int(input("Digite um número: "))

y = 1
while y <= n:
    if y%2 !=0:
        print(y)
    y += 1

os.system("pause")
