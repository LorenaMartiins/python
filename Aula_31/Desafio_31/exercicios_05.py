# Faça um programa que gere as tabuadas do 1 até o 10.

import os

for x in range(1, 11):
    for y in range(11):
        print(x,"x",y,"=",x*y)
    print("------------------")

os.system("pause")
