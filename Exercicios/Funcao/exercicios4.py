n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
op = input("Escolha a operação (| + | - | * | / |):")

operadores = {
    "+": lambda n1, n2: n1 + n2,
    "-": lambda n1, n2: n1 - n2,
    "*": lambda n1, n2: n1 * n2,
    "/": lambda n1, n2: n1 / n2
}

calculo = operadores[op]

print("O resultado é", calculo(n1, n2))

