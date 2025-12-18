def contar(n):
    contador = 0
    soma = n
    while contador < n:
        soma += contador
        contador += 1
    return soma

numero = int(input("Digite um numero:"))

print(f"A soma de 1 a {numero} é:", contar(numero))
