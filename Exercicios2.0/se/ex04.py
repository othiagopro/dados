print("---------- Calculo IMC ----------")

peso = float(input("Digite o peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * 2)

if imc < 18.5:
    print(f"Seu ICM foi {imc}! Você está abaixo do peso...")
elif imc >= 18.5 and imc < 25:
    print(f"Seu ICM foi {imc}! Você está no peso ideal...")
elif imc >= 25 and imc < 30:
    print(f"Seu ICM foi {imc}! Você está com sobrepeso...")
elif imc >= 30 and imc < 40:
    print(f"Seu ICM foi {imc}! Você está obeso...")
else:
    print(f"Seu ICM foi {imc}! Você está com obesidade mórbida...")