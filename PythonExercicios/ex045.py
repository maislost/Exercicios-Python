from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''ESCOLHA UMA DAS OPCOES ABAIXO
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input("Qual e a sua jogada? "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)
print("-=" * 21)
print(f"Voce jogou {itens[jogador]}")
print(f"O computador jogou {itens[computador]}")
print("-=" * 21)
if computador == 0:
    if jogador == 0:
        print("EMPATE!!!")
    elif jogador == 1:
        print("VOCE VENCEU!")
    elif jogador == 2:
        print("VOCE PERDEU!!!")
    else:
        print("JOGADA INVALIDA!!!")
elif computador == 1:
    if jogador == 0:
        print("VOCE PERDEU!!!")
    elif jogador == 1:
        print("EMPATE!!!")
    elif jogador == 2:
        print("VOCE VENCEU!!!")
    else:
        print("JOGADA INVALIDA!!!")
elif computador == 2:
    if jogador == 0:
        print("VOCE VENCEU!!!")
    elif jogador == 1:
        print("VOCE PERDEU!!!")
    elif jogador == 2:
        print("EMPATE!!!")
    else:
        print("JOGADA INVALIDA!!!")