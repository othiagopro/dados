def desconto(x, n):
    return x * n / 100
porc = int(input("Digite a porcentagem do desconto:"))
valor = float(input("Digite o valor da compra:"))

desc = (desconto(valor, porc))
calculo = lambda a, b: a - b

print("O desconto aplicado é: ", calculo(valor, desc))