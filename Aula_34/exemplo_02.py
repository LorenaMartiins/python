import os

nome = 'teste.txt'

arq = open('teste.txt', 'r')

# mostra o número de caracteres
print(arq.read(5))

# mostra a linha do arquivo
print(arq.readline())

# fecha o arquivo
arq.close()

os.system("pause")