from random import randint
v = 0
while True:
    jogador = int(input("Jogue um Numero de 0 a 10: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar ? [P/I]')).strip().upper()[0]
    print(f"Voce jogou {jogador} e o computador {computador}. Total de {total}.")
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador Ganhou!!!')
            v += 1
        else:
            print("VOCE PERDEU!!!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!!!')
            break
print('VAMOS JOGAR MAIS UMA VEZ...')
print(f"FIM DE JOGO! VOCE VENCEU {v} VEZES")



    