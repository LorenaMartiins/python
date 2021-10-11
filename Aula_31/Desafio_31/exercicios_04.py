# Faça um programa que mostre todos os números pares de 1 até 200.

import os

y = 1
while y <= 201:
    if y%2 != 1:
        print(y)
    y += 1

os.system("pause")
