import os

nome = 'textp.txt'

if os.path.exists(nome):
  os.remove(nome)
  print('Arquivo apagado com sucesso!!')
else:
  print("Arquivo não foi encontrado!!")

os.system("pause")