def contagem(a, b, c):
    print(f"Contagem de {a} até {b} de {c} em {c}")
    for i in range(a, b+1, c):
        print(f"{i}")


contagem(1, 10, 1)
contagem(10, 0, -2)

print("Agora é sua vez de personalizar")
inicio = int(input("Inicio: "))
fim = int(input("Fim:"))
passo = int(input("Passo: "))
contagem(inicio, fim, passo)