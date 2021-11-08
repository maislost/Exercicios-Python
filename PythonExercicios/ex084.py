pessoas = []
peso = []
maior_peso = menor_peso = 0
while True:
    peso.append(str(input('Nome: ')))
    peso.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = peso[1]
    else:
        if peso[1] > maior_peso:
            maior_peso = peso [1]
        if peso[1] < menor_peso:
            menor_peso = peso[1]
    pessoas.append(peso[:])
    peso.clear()
    r = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-=' * 30) 
print(f'Ao final tivemos {len(pessoas)} cadastradas!')
print(f'O maior peso foi de {maior_peso}')
for i in pessoas:
    if peso[1] == maior_peso:
        print(f'{peso[0]}')
print(f'O menor peso foi de {menor_peso}')
for i in pessoas:
    if peso [1] == menor_peso:
        print(f'{peso[0]}')

