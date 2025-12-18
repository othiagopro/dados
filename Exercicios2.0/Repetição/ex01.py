maiores = []
menores = []


for ano in range(1, 3):
    idade = int(input("Digite o seu ano de nascimento: "))
    maioridade = 2025 - ano
    if maioridade >= 18:
        maiores.append(idade)
    elif maioridade < 18: 
        menores.append(idade)
    continue

print(f"Maiores de idades: {maiores}")
print(f"Menores de idades: {menores}")
