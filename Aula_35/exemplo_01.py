import os, requests

# Fazendo a requisição da página para o servidor
url = requests.get('https://pt.wikipedia.org/wiki/Tom_Holland_(ator)')

# Status da requisição
print("Status: ",url.status_code,"\n")

# Verificando o header da página
print("header: ", url.headers,"\n")

#Verificando o HTML da página
print("HTML: ", url.content,"\n")

os.system("pause")