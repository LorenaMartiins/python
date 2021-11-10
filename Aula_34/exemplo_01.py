import os

# Usuario digitar seu arquivo
# nome = input("Digite o nome do arquivo: ")
# nome = nome+ '.txt'

#nome do arquivo
nome = 'teste.txt'

if os.path.exists(nome):
  #abrindo um arquivo em modo de leitura
  arq = open(nome, 'r')
  #mostra o conteúdo do arquivo
  print(arq.read())
else:
  print("Arquivo não foi encontrado!!")

os.system("pause")