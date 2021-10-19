import os

# Exemplo de função com N argumentos
def lista_nomes(*nomes):
  print(nomes)

# Chamando uma função com N argumentos
lista_nomes("Jubileu", "Maria", "Anna", "Lucas")
lista_nomes("Paulo", "Fernanda", "Julia")

os.system("pause")