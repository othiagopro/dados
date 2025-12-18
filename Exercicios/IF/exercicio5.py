valor_despesa = float(input("Digite o total de despesas no mês:"))
print(f"Seu gasto foi de R${valor_despesa}")
if valor_despesa > 3000:
    print(f"Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do limite estabelecido")