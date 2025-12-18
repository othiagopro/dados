from time import sleep
from random import randint
from operator import itemgetter

temp = {}

temp["jogador1"] = randint(1, 6)
temp["jogador2"] = randint(1, 6)
temp["jogador3"] = randint(1, 6)
temp["jogador4"] = randint(1, 6)
princ = list(sorted(temp.items(), key=itemgetter(1), reverse = True))
print(princ)

print("Valores sorteados:")
for k, v in temp.items():
    print(f"   O {k} tirou {v}")
    sleep(0.5)

print("Ranking dos jogadores: ")
for i, v in enumerate(princ):
    print(f"   {i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)





