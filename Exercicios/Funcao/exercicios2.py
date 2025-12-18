def filtro(n):
    return n % 2 == 0

numeros = input("Digite os números separados por espaço:").split()
numeros = list(map(int, numeros))

resultado = list(filter(filtro, numeros))

print("Numeros pares: ", resultado)