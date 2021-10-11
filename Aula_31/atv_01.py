import os

#tabuada
n = int(input("Digite um número: "))

#for x in range(11):
#    print(n,"x",x,"=",n*x)

x = 1
while x <= 10:
    print(n,"x",x,"=",n*x)
    x += 1

os.system("pause")