from random import randint
print("----" * 20)
print("Bem vindos ao desafio do milenium!!!!")
computador = randint(0, 5)
print("Advinhe o numero secreto de 0 a 5")
jogador= int(input("Escolha seu numero agora:  "))

if jogador == computador:
    print(f"Parabens! voce acertou o numero secreto {computador}")
    print("Voce venceu o jogo do milenium!")
else:
    print("Voce errou!!!!!")
    print(f"O numero secreto era {computador}")

print("Fim de jogo!")
print("----" * 20)