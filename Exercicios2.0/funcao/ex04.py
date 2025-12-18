def linha():
    print("-=" * 20)

def maior(*numeros):
    maior_atual = numeros[0]
    linha()
    print("Analisando os valores passados...")
    for num in numeros:
        if num > maior_atual:
            maior_atual = num
    print(maior_atual)
    

maior(1, 2, 20, 9)