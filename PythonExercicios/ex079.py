listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor Adicionado Com Sucesso...')
    else:
        print('Não é possível adicionar valores duplicados.')

    r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('=-' * 30)
print(f'{listanum}')
