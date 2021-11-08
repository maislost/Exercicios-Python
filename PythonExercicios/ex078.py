listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f"Digite um Numero na posição {c}: ")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
             maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores: {listanum}')
print(f'O maior número foi {maior} na posição ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f" O Menor número foi {menor} na posição ", end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
