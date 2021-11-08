numeros = []
while True:
    n = int(input('Digite um Valor: '))
    numeros.append(n)
    r = str(input('Voce quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Foram digitados {len(numeros)} números!')
numeros.sort(reverse=True)
print(f'Em Ordem Decrescente {numeros}')
if 5 not in numeros:
    print('O Valor 5 nao está na lista!')
else:
    print('O valor 5 esta na lista!')
