# Faça um programa que mostre uma contagem regressiva que inicia em 10 e termina em 0.

import os

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)

os.system("pause")
