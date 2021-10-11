import os

#faz as tabuadas do 1 ao 10
for x in range(1, 11):
    #faz a estrutura da tabuada
    for y in range(11):
        print(x,"x",y,"=",x*y)
    print("------------------")
    
os.system("pause")