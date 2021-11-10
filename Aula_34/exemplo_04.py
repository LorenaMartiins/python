import os

# Abre o arquivo ou cria um nome em modo de anexo 
arq_w = open("texto.txt", 'a')

texto = input('Digite um texto: ')
arq_w.write(texto+'\n' )

arq_w.close()

# Abre o arquivo em modo de leitura
arq_r = open('texto.txt', 'r')
print(arq_r.read())

os.system("pause")