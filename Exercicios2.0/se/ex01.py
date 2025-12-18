ano = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

c = 18
idade = ano_atual - ano
tempo = c - idade

if idade == 18:
    print(f"Você tem {idade} anos, já é hora de se alistar!")
elif idade < 18:
    print(f"Você tem {idade} anos, ainda falta {tempo} anos para se alistar!")
else:
    print(f"Você tem {idade} anos, já passou o tempo de se alistar")