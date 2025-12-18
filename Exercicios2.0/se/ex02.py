n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))

m = (n1 + n2) / 2

if m < 5:
    print(f"Sua média foi {m}, você está reprovado!")
elif m > 5 and m <= 6.9:
    print(f"Sua média foi {m}, você está de recuperação!")
else:
    print(f"Sua média foi {m}! Parabéns você foi aparovado!")