from random import randint
lista = []
jogos = []
cont = 0
tot = 1
quant = int(input('Quantos jogos você deseja realizar? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(f'Sorteando {quant} jogos...')
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
