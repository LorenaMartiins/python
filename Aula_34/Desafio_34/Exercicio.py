# Um programa em Python que conte o número de vogais em um arquivo de texto.

import os

nome = 'musica.txt'
cont = 0

if os.path.exists(nome):
  arq = open(nome, 'r')

  musica = arq.read().replace(' ','')

  for a in range(len(musica)):
    if musica[a] == 'a' or musica[a] == 'A':
      cont += 1    
  print('O numero de letras A: ', cont)

  for a in range(len(musica)):
    if musica[a] == 'e' or musica[a] == 'E':
      cont += 1    
  print('O numero de letras E: ', cont)

  for a in range(len(musica)):
    if musica[a] == 'i' or musica[a] == 'I':
      cont += 1    
  print('O numero de letras I: ', cont)

  for a in range(len(musica)):
    if musica[a] == 'o' or musica[a] == 'O':
      cont += 1    
  print('O numero de letras O: ', cont)

  for a in range(len(musica)):
    if musica[a] == 'u' or musica[a] == 'U':
      cont += 1    
  print('O numero de letras U: ', cont)  
else:
  print("Arquivo não encontrado")

os.system("pause")