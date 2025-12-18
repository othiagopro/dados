def linha():
    print("-=" * 30)

def contagem(inicio, fim, passo):
    if passo == 0:
        passo == 1
    if passo == -1:
        passo *= -1
    linha()
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    cont = 0
    while inicio <= fim:
        print(cont)
        cont += passo

contagem(1, 10, 1)

