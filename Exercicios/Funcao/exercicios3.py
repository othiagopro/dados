produtos = input("Digite os produtos separados por vírgula: ").split(", ")
preco = input("Digite os preços separados por vírgula: ").split(", ")
# resultado = list(zip(produtos, preco))

for produtos, preco in zip(produtos, preco):
    print(f"{produtos.strip()}: {preco.strip()}")