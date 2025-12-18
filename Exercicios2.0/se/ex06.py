from random import randint
print("[1] Papel\n[2] Tesoura\n[3] Pedra\n")

computador = randint(1, 3)
if computador == 1:
    print("Papel")
elif computador == 2:
    print("Tesoura")
else: 
    print("Pedra")

jogador = input("Escolha: ")

if computador == jogador:
    print("Empate") 


