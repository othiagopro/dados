def conversor(valor):
    return int(valor)

def somar(valores):
    total = 0 
    for v in valores:
        num = conversor(v)
        if num is None:
            return f"Erro: {v} não é um numero"
        total += num
    return total

vendas = input("Digite o valor das vendas:")
valores = vendas.split()

resultado = somar(valores)

print(resultado)


