from time import sleep
from random import randint
computador = randint(1, 10)
print("Sou seu computador...")
print("Acabei de pensar em um numero de 1 a 10 hahahaha!")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Eai? Consegue Acertar? Escolhe um numero logo! "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Um Pouco Maior ....")
        elif jogador > computador:
            print("Um pouco menor...")
        else:
            print("Opcao Invalida")

print(f"Acertou!!! Com {palpites} tentativas!")
