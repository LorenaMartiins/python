import os, requests
from bs4 import BeautifulSoup

# Fazendo a requisição do site para o servidor
url = requests.get('https://www.shueisha-mteixeira.com.br/')

# Guardando o conteúdo HTML em uma variável
html = url.content

# Usando a bibloteca BeautifulSoup para organizar o HTML
site = BeautifulSoup(html,'html.parser')

# Exibindo o código HTML com identação
print(site.prettify())

os.system("pause")