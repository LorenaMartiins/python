import os

nome = 'texto.txt'
cont = 0

if os.path.exists(nome):
  arq = open(nome, 'r')

  texto = arq.read()

  for x in range(len(texto)):
    if texto[x] == 'a' or texto[x] == 'A':
      cont += 1
  
  print('O numero de letras: ', cont)
else:
  print("Arquivo não encontrado")

os.system("pause")