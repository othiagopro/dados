peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura (m):"))

imc = peso / (altura ** 2)
print(f"Seu IMC é :{imc}")
if imc < 18.5:
    print(f"Você está abaixo do peso")
elif 18.5 <= imc < 25:
    print("Você está com o peso em dia")
else:
    print("Você está acima do peso! Procure um médico")