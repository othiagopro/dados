nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

with open('./dados/dados.txt', 'w') as t:
    t.write(f'Nome: {nome}\n')
    t.write(f'Idade: {idade}\n')
    