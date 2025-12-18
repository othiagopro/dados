atividade_a = int(input("Informe os dias para a Atividade A:"))
atividade_b = int(input("Informe os dias para a Atividade B:"))
atividade_c = int(input("Informe os dias para a Atividade C:"))

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    tempo_total = atividade_a + atividade_b + atividade_c
    print(f"O numero de dias utilizados foi {tempo_total} dias")
