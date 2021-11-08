lista = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco')
while True:
    num = int(input("Escolha um Numero entre 0 e Cinco: "))
    if num > 5:
        num = int(input('Opcao Invalida. Digite novamente um numero entre 0 e 5: '))
    print(f'Voce digitou o numero {lista[num]}')
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('Fim do Programa....')

