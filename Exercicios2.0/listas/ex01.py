temp = []
princ = []
mai = men = 0
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))
    
    princ.append(temp[:])
    temp.clear()
    r = input("Quer continuar? [S/N]")
    if r == "n":
        break

print(f"Ao todo, você cadastrou {len(princ)} pessoas.")