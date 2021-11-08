ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    r = str(input('Deseja continuar? [S/N]'))
    if r not in 'Ss':
        break
print('=-' * 30)
print(f'{"No." :< 4}{"Nome" :< 10}{"Media" :>8}')
print('=-' * 30)

