import os

nome = 'texto.txt'
cont = 0

if os.path.exists(nome):
  arq = open(nome, 'r')

#                    conta só as letras
  texto = arq.read().replace(' ','')

  for x in range(len(texto)):
      cont += 1
  
  print('O numero de caracteres: ', cont)

else:
  print("Arquivo não encontrado!!")

os.system("pause")