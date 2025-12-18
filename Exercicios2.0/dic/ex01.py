alunos = {}
for c in range(0, 1):
    alunos["Nome"] = input("Nome: ")
    alunos["Média"] = float(input(f"Média de {alunos['Nome']}: "))
    if alunos["Média"] > 6:
        alunos["Situação"] = "Aprovado"
    elif alunos["Média"] < 6:
        alunos["Situação"] = "Reprovado"
for k, v in alunos.items():
    print(f"{k} é igual a {v}")