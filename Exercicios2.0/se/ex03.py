from random import randint

computador = randint(1, 10)
acertou = False 
palpites = 0

print("Prazer eu sou o Roberty...")
print("Pensei em um numero de 1 a 10... Tente acertar! \n")

while not acertou:
    jogador = int(input("Qual é o seu chute? "))
    palpites += 1
    if jogador == computador:   
        acertou = True
    else:
        if jogador > computador:
            print("Menos... Tente novamente!")
        elif jogador > 10:
            print("Numero invalido... Tente novamente")
        else:
            print("Mais... Tente novamente!")
        
print(f"Acertou! Você conseguiu em {palpites} tentativas!")