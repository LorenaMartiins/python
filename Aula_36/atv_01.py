import os, openpyxl
from openpyxl.styles import Border, Side, Alignment

planilha = openpyxl.Workbook()

page = planilha['Sheet']
page.title = 'Alunos'

n_cadastros = int(input("Digite um número de cadastros: "))

page.append(['NOME', 'IDADE', 'TURMA'])

for x in range(n_cadastros):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  turma = input("Digite sua turma: ") 
  print(" ")
  page.append([nome, idade, turma ])

planilha.save('Alunos.xlsx')

os.system("pause")