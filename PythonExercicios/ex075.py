num = (int(input('Digite um Numero:')),
       int(input('Digite outro  Numero:')),
       int(input('Digite mais um Numero:')),
       int(input('Digite o ultimo Numero:')),)
print(num)
print(f'O Numero 9 pareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 esta na posicao {num.index(3)+1}')
else:
    print('O numero nao aparece na lista.')
print(f'Os Seguintes Numeros sao Pares: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')

