import csv

alunos = ['João', '7', 'Pedro', '8', 'Maria', '6']

with open('./dados/alunos.csv', 'w', newline='') as t:
    escritor = csv.writer(t)
    for i in range(0, len(alunos), 2):
        escritor.writerow([alunos[i], alunos[i+1]])

with open('./dados/alunos.csv', 'r') as t:
    leitor = csv.reader(t)
    for linha in leitor:
        if int(linha[1]) >= 7:
            print(f'Aluno: {linha[0]} - Nota: {linha[1]} - Aprovado')