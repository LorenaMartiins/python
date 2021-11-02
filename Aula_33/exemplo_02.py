import os

lista = ['Jubileu', 'Maria', 'Lucas', 'Ana', 'Julia']

# mostra valores da lista usando for
for x in range(5):
  print(lista[x])

print('-------------')

# mostra valores da lista ao contrario, usando o while
y = 4
while y >= 0:
  print(lista[y])
  y-=1

os.system("pause")