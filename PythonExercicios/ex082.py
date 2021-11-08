num = list()
numPar =  list()
numImpar = list()
while True:
    num.append(int(input('Digite um Valor: ')))
    r = str(input('Deseja digitar mais um valor? [S/N] ')).strip().upper()[0]
    if r  in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        numPar.append(v)
    elif v % 2 == 1:
        numImpar.append(v)
print(f'Os Valores digitados foram: {num}')
print(f'Os valores pares são {numPar}')
print(f'Os valores impares são {numImpar}')

