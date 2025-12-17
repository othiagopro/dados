# Escrever um arquivo com a função open()
# write (w) serve para escrever o arquivo, quando vamos escrever precisamos passar dois parametros ('dados.txt', 'w') nesse caso criamos o txt e passamos o paramentro (w) indicando que estamos escrevendo
# Read (r) serve para ler o arquivo!
# (a) serve para adicionar algo na ultima linha sem sobrescrever 

# TXT - Serve para salvar log dos registros, coisas mais simples, não pesa tanto no PC
# CSV - Serve para grande quantidades de dados
# JSON - Converter JSON para dict e vice versa

#                  TXT
with open('./dados/dados.txt', 'w') as t:
    t.write('Teste, estou testando essa função, legal funcionou, teste')

with open('./dados/dados.txt', 'a') as t:
    t.write('Ultima linha')

with open('./dados/dados.txt', 'r') as t:
    conteudo = t.read()
    print(conteudo)

#                 CSV
import csv

with open('./dados/dados.csv', 'w') as t:
    escritor = csv.writer(t)
    escritor.writerow(['nome', 'idade'])
    escritor.writerow(['Thiago', '22'])
    escritor.writerow(['Janderson' '55'])

with open('./dados/dados.csv', newline='') as t:
    leitor = csv.reader(t)
    for linha in leitor:
        print(linha)

#                JSON
import json

dados = {'nome': 'Thiago', 'idade': '22', 'enderecos':['a','b']}
with open('./dados/dados.json', 'w') as t:
    json.dump(dados, t)

with open('./dados/dados.json', 'r') as t:
    dados_lidos = json.load(t)
    print(dados_lidos)