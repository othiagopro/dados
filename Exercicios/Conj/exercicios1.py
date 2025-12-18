dicionario_produtos = {}

for i in range(3):
    nome = input("Digite o nome do produto:")
    qtd = int(input("Digite a quantidade:"))

    dicionario_produtos[nome] = qtd
print(f"Dicionario de produtos: {dicionario_produtos}")

