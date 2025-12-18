estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

nome_produto = input("Nome do produto a ser atualizado: ")
nova_quantidade = int(input("Nova quantidade:"))

estoque[nome_produto] = nova_quantidade
print(f"Estoque atualizado: {estoque}")
