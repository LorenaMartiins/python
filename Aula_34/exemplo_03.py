import os

# Abre o arquivo ou cria um novo em modo de escrita
arq = open('texto.txt', 'w')

# Pedindo para digitar um texto
texto = input("Digite um texto: ")
#Gravando o texto digitado no Arquivo
arq.write(texto)

# Fechando o arquivo
arq.close()

os.system("pause")