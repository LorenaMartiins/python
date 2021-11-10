import os

# Abre o arquivo ou cria um arquivo em modo de anexo
arq = open('indx.html', 'a')

html = '<h1> Hello world <h1>'

arq.write(html)
arq.close()

os.system("pause")