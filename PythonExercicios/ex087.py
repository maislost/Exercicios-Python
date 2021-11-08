matriz = [[0,0,0], [0,0,0], [0,0,0]]
valores_pares = maior_valor = soma_coluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l},{c}: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            valores_pares += matriz[l][c]
    print()
print('-=' *30)
print(f'A soma dos valores pares é: {valores_pares} ')
for l in range(0,3):
    soma_coluna += matriz[l][2]
print(f'A soma da Coluna 2 é: {soma_coluna} ')
for l in range(0,3):
    if c == 0:
        maior_valor = matriz[1][c]
    elif matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da linha 2 é: {maior_valor}')
