import os

n = int(input("Digite um número: "))

y = 1
while y <= n:
    if y%2 !=0:
        print(y)
    y += 1

os.system("pause")